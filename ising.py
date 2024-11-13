import numpy as np
import matplotlib.pyplot as plt



from init import *
from wolff import *
from single_flip import *
    

flipLogic = wolffFlip


if __name__ == '__main__':
    N = 100
    ising = initializeIsing(N)
    Js = initializeJ(N, "Ones")
    Es = []
    temp = 3
    Emin = calculateEnergy(np.abs(ising), Js)


    numRuns = 500
    for i in range(numRuns):
        temp = temp - 3/800
        print(i)
        for j in range(100):
            ising = flipLogic(ising, Js, temp)
        Es.append(calculateEnergy(ising, Js))

    plt.scatter(range(numRuns), Es, s = 12)
    plt.axhline(Emin)
    plt.show()
    plt.imshow(ising)
    plt.show()