
from init import *
import numpy as np

def flipSingleSpin(ising, spot):
    tempIsing = ising.copy()
    i = spot[0]
    j = spot[1]
    tempIsing[i,j] = -tempIsing[i,j]
    return tempIsing

def getProbUpdate(ising_i, spin_loc, J_arr, temp):

    # de = 2 J s_here * sum(neighbor_spins)
    neighbors = getNeighbors(ising_i, spin_loc)
    de = 0
    sk = ising_i[spin_loc[0], spin_loc[1]]

    for i in range(4):
        pair = neighbors[i]
        if pair:
            sj = ising_i[pair[0], pair[1]]
            jConnect = getJfromNum(i, spin_loc, J_arr)
            de += jConnect * sj * sk
          
    if de < 0:
        return 1
    else:
        beta = 1/temp
        exponent = - beta * 2 * de
        prob = np.exp(exponent)
        return prob
    
def updateSpin_single(ising, spin_loc, J_arr, temp):
    prob = getProbUpdate(ising, spin_loc, J_arr, temp)
    if np.random.random() < prob :
        return flipSingleSpin(ising, spin_loc)
    return ising

def singleFlipLogic(ising, J_arr, temp):
    spin_loc = pickRandomSpot(ising)
    return updateSpin_single(ising, spin_loc, J_arr, temp)

