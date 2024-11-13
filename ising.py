## Making sure that the standard ising model works as expected - ish
import numpy as np
import matplotlib.pyplot as plt

from init import *
from wolff import *
from single_flip import *
    

flipLogic = singleFlipLogic


if __name__ == '__main__':
    N = 30
    ising = initializeIsing(N)
    Js = initializeJ(N, "Ones")
    Es = []
    Ms = []
    Ms2 = []
    betas = []
    Emin = calculateEnergy(np.abs(ising), Js)
    Mmin = calculateMagnetism(np.abs(ising))

    
    temps = np.linspace(0.1, 10, 80)
    for temp in temps:
        ising = initializeIsing(N)
        ising2 = initializeIsing(N)
        print(temp)
        for j in range(50000):
            ising = flipLogic(ising, Js, temp)
            ising2 = flipLogic(ising2, Js, temp)
        # Es.append(calculateEnergy(ising, Js)/(N*N))
        Ms.append(calculateMagnetism(ising)/(N*N))
        Ms2.append(calculateMagnetism(ising2)/(N*N))
        betas.append(1/temp)

    fig, ax1 = plt.subplots()
    # Creating a secondary y-axis for Ms
    ax1.scatter(temps, np.abs(Ms), s=12, c='g', label='Ms')
    ax1.scatter(temps, np.abs(Ms2), s=12, c='r', label='Ms')
    ax1.set_ylabel('Ms', color='g')

    # plt.axhline(Emin)
    plt.show()
    plt.imshow(ising)
    plt.show()