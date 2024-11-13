import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.tsa.stattools as stattools

from init import *
from single_flip import *


flipLogic = singleFlipLogic




if __name__ == '__main__':
    N = 30
    ising = initializeIsing(N)
    Js = initializeJ(N, "pm")

    temps = np.linspace(10,.1, 100)

    betas = np.linspace(1/.25, 1/5, 500)
    temps = 1/betas

    runsPerTemp = 500

    ac_t_E = []
    ac_t_M = []

    for temp in temps:
        print(temp)
        Es = []
        Ms = []
        for i in range(runsPerTemp):
            ising = flipLogic(ising, Js, temp)
            Ms.append(calculateEnergy(ising, Js))
            # Ms.append(calculateMagnetism(ising))
        acf_values = stattools.acf(Ms, nlags=40)
        M_autocorr_time = 1 + 2 * np.sum(acf_values[1:])
        ac_t_M.append(M_autocorr_time)

        # E_autocorr_time = autocorrelation_time(Es)
        # ac_t_E.append(E_autocorr_time)

    # plt.scatter(betas, ac_t_E, c = "r", s = 12)
    plt.plot(betas, ac_t_M, c = "b")
  
    plt.show()
    plt.imshow(ising)
    plt.show()




