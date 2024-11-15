# Order parameters qEA and qAB:

#  qEA = lim(t->large)  1/N sum (i) : ⟨si(0) si(t)⟩ 
#  qEA_l = 1/N_bonds * sum s1i * s1j * s2i * s2j
#  qAB =1/N Sum (i) s(a)·s(b), where s(a) and s(b) are from models that started identical and evolved separately

import numpy as np
import matplotlib.pyplot as plt

from init import *
from single_flip import *
    

flipLogic = singleFlipLogic

def calc_qAB(ising1, ising2):
    N = len(ising1[0])
    sum = 0
    for i in range(N):
        for j in range(N):
            ds = ising1[i][j] * ising2[i][j] 
            sum = sum + ds
    return sum/(N*N)

def calc_qAB_l(ising1, ising2):
    N = len(ising1[0])
    sum = 0
    for i in range(N):
        for j in range(N):
            ds1, ds2 = 0, 0
            if (i != N-1):
                ds1 = ising1[i][j] * ising2[i][j] * ising1[i+1][j] * ising2[i+1][j] 
            if (j != N-1):
                ds2 = ising1[i][j] * ising2[i][j] * ising1[i][j+1] * ising2[i][j+1] 
            sum = sum + ds1 + ds2
    return sum/(2*N*N)

def analytic_qAB_l(energy, temp):
    #Second calculation of qAB_l. Requires that J is gaussian w variance = var
    var = 1
    z = 4 # 4 neighbors bonded
    num = np.abs(energy) * temp
    denom = (z/2)*var
    return 1 - num/denom


if __name__ == '__main__':
    N = 50
    ising1 = initializeIsing(N)
    ising2 = initializeIsing(N)
    Js = initializeJ(N, "gaus")
    temp = .5
    measure_points = np.array([1e4, 5e4, 1e5,3e5, 5e5, 7e5, 1e6, 2e6, 5e6, 8e6, 1e7, 1.5e7])
    qSims = np.zeros_like(measure_points)
    qanalitics = np.zeros_like(measure_points)

    numRuns = 5
    for runs in range(numRuns):
        i = 0
        ising1 = initializeIsing(N)
        ising2 = initializeIsing(N)
        Js = initializeJ(N, "gaus")
        while i < measure_points[-1]:
            i = i + 1
            ising1 = flipLogic(ising1, Js, temp)
            ising2 = flipLogic(ising2, Js, temp)

            if i in measure_points:
                index = np.where(measure_points == i)[0][0]  # Get the index using NumPy
                print(i)
                qSim = calc_qAB_l(ising1, ising2)

                E1 = calculateEnergy(ising1, Js)/(N*N)
                E2 = calculateEnergy(ising2, Js)/(N*N)
                q_analytic_1 = analytic_qAB_l(E1, temp)
                q_analytic_2 = analytic_qAB_l(E2, temp)
                qan = (q_analytic_1 + q_analytic_2) / 2
                qSims[index]= qSims[index] + (qSim/numRuns)
                qanalitics[index]= qanalitics[index] + (qan/numRuns)

    plt.scatter(measure_points, qSims, s = 12, c = "r", label = "Simulated Points")
    plt.scatter(measure_points, qanalitics, s = 12, c = "g", label = "Calculated Points")
    plt.xscale('log')  # Set x-axis to logarithmic scale
    plt.legend()
    plt.show()
    



