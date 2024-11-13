
import numpy as np

#    N x N spin matrix
#    spin[i,j] connects to spin[i+1, j] w strength J_down[i,j]
#    spin[i,j] connects to spin[i, j+1] w strength J_right[i,j]
    

def initializeIsing(N):
   
    isingSpins = np.random.choice([-1, 1], size=(N, N))
    
    return isingSpins

def initializeJ(N, rule = "Ones"):
    if rule == "Ones":
        J_down = np.ones((N-1, N))
        J_right = np.ones((N, N-1))
    if rule == "pm":
        J_down = np.random.choice([-1, 1], size=(N-1, N))
        J_right = np.random.choice([-1, 1], size=(N, N-1))
    if rule == "gaus":
        std = 1
        J_down = np.random.normal(loc=0, scale=std, size=(N-1, N))
        J_right = np.random.normal(loc=0, scale=std, size=(N, N-1))

    return (J_down, J_right)

def calculateEnergy(ising, J_arr):
    N = len(ising[0])
    Esum = 0
    for i in range(N):
        for j in range(N):
            contributiondown = 0
            contributionright = 0
            if i != (N-1):
                contributiondown  = J_arr[0][i, j] * ising[i, j] * ising[i+1, j] 
            if j != (N-1):
                contributionright = J_arr[1][i, j] * ising[i, j] * ising[i, j+1]
            contribution_tot = contributiondown + contributionright
            Esum = Esum - contribution_tot
    return Esum

def pickRandomSpot(ising):
    N = len(ising[0])
    i = np.random.randint(0,N)
    j = np.random.randint(0,N)
    return (i,j)


def getNeighbors(ising, spot):
    ## spot = (i, j)
    ## return [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
    N = len(ising[0])
    i = spot[0]
    j = spot[1]
    if (j != N-1):
        s1 = (i, j+1)
    else:
        s1 = None

    if (j != 0):
        s2 = (i, j-1)
    else:
        s2 = None

    if (i != N-1):
        s3 = (i+1, j)
    else:
        s3 = None

    if (i != 0):
        s4 = (i-1, j)
    else:
        s4 = None

    return [s1, s2, s3, s4]

def getJfromNum(dir, spot, J_arr):

    # dir = 0,1,2,3
    # 0 - J_down[i,j]
    # 1 - J_down[i-1, j]
    # 2 - J_right[i, j]
    # 3 - J_right[i, j-1]

    N = len(J_arr[0][0])
    i = spot[0]
    j = spot[1]
    J_down = J_arr[0]
    J_right = J_arr[1]
    if dir == 0:
        if (j != N-1):
            return J_right[i, j]
        else:
            return 0
    elif dir == 1:
        if (j != 0):
            return J_right[i, j-1]
        else:
            return 0
    elif dir == 2:
        if (i != N-1):
            return J_down[i,j]
        else:
            return 0
    elif dir == 3:
        if (i != 0):
            return J_down[i-1, j]
        else:
            return 0
    else:
        return None