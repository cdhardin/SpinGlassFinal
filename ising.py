## Making sure that the standard ising model works as expected - ish
import numpy as np
import matplotlib.pyplot as plt

from init import *
from wolff import *
from single_flip import *
    

flipLogic = singleFlipLogic

def runModel(ising, Js, temp, n):
    for i in range(n):
        ising = flipLogic(ising, Js, temp)
    return ising

if __name__ == '__main__':
    N = 30


    Js = initializeJ(N, "Ones")
    ising_Tlow = runModel(initializeIsing(N), Js, 0.000001, 100_000)
    ising_THigh = runModel(initializeIsing(N), Js, np.inf, 100_000)

    ElowT = calculateEnergy(ising_Tlow, Js)
    MlowT = calculateMagnetism(ising_Tlow)
    EhighT = calculateEnergy(ising_THigh, Js)
    MhighT = calculateMagnetism(ising_THigh)
    print("J = 1")
    print(f"Temp = 0 : ")
    print(f"Expected E = -2, M = 1")
    print(f"Calculated E = {ElowT/(N*N)}, M = {MlowT/(N*N)}")
    print(f"Temp = inf : ")
    print(f"Expected E = 0, M = 0")
    print(f"Calculated E = {EhighT/(N*N)}, M = {MhighT/(N*N)}")

   

    Js = initializeJ(N, "-1")
    ising_Tlow = runModel(initializeIsing(N), Js, 0.000001, 100_000)
    ising_THigh = runModel(initializeIsing(N), Js, np.inf, 100_000)

    ElowT = calculateEnergy(ising_Tlow, Js)
    MlowT = calculateMagnetism(ising_Tlow)
    EhighT = calculateEnergy(ising_THigh, Js)
    MhighT = calculateMagnetism(ising_THigh)
    print("J = -1")
    print(f"Temp = 0 : ")
    print(f"Expected E = -2, M = 0")
    print(f"Calculated E = {ElowT/(N*N)}, M = {MlowT/(N*N)}")
    print(f"Temp = inf : ")
    print(f"Expected E = 0, M = 0")
    print(f"Calculated E = {EhighT/(N*N)}, M = {MhighT/(N*N)}")
 
    N=50
    plt.imshow(runModel(initializeIsing(N), initializeJ(N), 1, 100_000)) 
    plt.show()

    # Js = initializeJ(N, "Ones")
    # ising1 = initializeIsing(N)
    # ising2 = initializeIsing(N)
    # Es = []
    # Ms = []
    # Ms2 = []
    # betas = []
    # # Emin = calculateEnergy(np.abs(ising), Js)
    # # Mmin = calculateMagnetism(np.abs(ising1))

    
    # temps = np.linspace(0.01, 5, 100)
    # for temp in temps:
    #     ising = initializeIsing(N)
    #     ising2 = initializeIsing(N)
    #     print(temp)
    #     for j in range(50000):
    #         ising1 = flipLogic(ising, Js, temp)
    #         ising2 = flipLogic(ising2, Js, temp)
    #     # Es.append(calculateEnergy(ising, Js)/(N*N))
    #     Ms.append(calculateMagnetism(ising1)/(N*N))
    #     Ms2.append(calculateMagnetism(ising2)/(N*N))
    #     betas.append(1/temp)

    # fig, ax1 = plt.subplots()
    # # Creating a secondary y-axis for Ms
    # ax1.scatter(temps, np.abs(Ms), s=12, c='g', label='Ms')
    # ax1.scatter(temps, np.abs(Ms2), s=12, c='r', label='Ms')
    # ax1.set_ylabel('Ms', color='g')

    # # plt.axhline(Emin)
    # plt.show()
    # plt.imshow(ising)
    # plt.show()
    # plt.imshow(ising2)
    # plt.show()