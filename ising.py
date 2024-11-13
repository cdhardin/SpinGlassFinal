import numpy as np
import matplotlib.pyplot as plt



from init import *
from single_flip import *
    

flipLogic = singleFlipLogic


if __name__ == '__main__':
    N = 100
    ising = initializeIsing(N)
    Js = initializeJ(N, "gaus")
    Es = []
    temp = 1
    Emin = calculateEnergy(np.abs(ising), Js)

    for i in range(500):
        print(i)
        for j in range(100):
            ising = flipLogic(ising, Js, temp)
        Es.append(calculateEnergy(ising, Js))

    plt.scatter(range(500), Es, s = 12)
    plt.axhline(Emin)
    plt.show()
    plt.imshow(ising)
    plt.show()