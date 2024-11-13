##Idea 1. adapted Wolff algorithm:

# instead of picking clusters with si = sj, pick clusters with J_si * si * sj > 1
# Other than that, same exact alogorithm

# 1. Choose a random spin as the initial cluster
# 2. If a neighboring spin is parallel to the initial spin it will be added to the cluster with probability 1 − exp(−2βJ).
#                             parallel is now defined as Jss > 0, instead of ss > 0
#                             This will not
# 3. Repeat step (2) for all points newly added to the cluster and repeat this procedure until no new points can be added.
# 4. Perform measurements using improved estimators
# 5. Flip all spins in the cluster

from init import *

def wolffFlip(ising, Js, temp):
    cluster = findCluster(ising, Js, temp)
    for c in cluster:
        ising[c[0]][c[1]] = -ising[c[0]][c[1]]
    return ising

#pickRandomSpot(ising) to pick starting spot

def addToCluster(ising, neighbor, spot, i, J_arr, temp):
    #Return True or False depending on if we're gonna add point to the cluster
    s1 = ising[spot[0]][spot[1]]
    s2 = ising[neighbor[0]][neighbor[1]]
    J = getJfromNum(i, spot, J_arr)
    bond = s1*s2*J
    if bond < 0: return False

    prob = np.exp(-2 * bond / temp) ## accept w prob 1-exp() so random > exp() accepts
    if np.random.random() > prob:
        return True
    return False

def addToCluster100percent(ising, neighbor, spot, i, J_arr):
    #Return True or False depending on if we're gonna add point to the cluster, True 100% of the time
    s1 = ising[spot[0]][spot[1]]
    s2 = ising[neighbor[0]][neighbor[1]]
    J = getJfromNum(i, spot, J_arr)
    return (s1*s2*J > 0)

def findCluster(ising, Js, temp):
    initialSpot = pickRandomSpot(ising)
    visitedPoints = {initialSpot}
    queue = [initialSpot]
    cluster = [initialSpot]
    while len(queue) > 0:
        spot = queue.pop(0)
        neighbors = getNeighbors(ising, spot)
        for i, neighbor in enumerate(neighbors):
            if neighbor:
                if neighbor in visitedPoints:
                    continue
                else:
                    visitedPoints.add(neighbor)
                    if addToCluster(ising, neighbor, spot, i, Js, temp):
                        cluster.append(neighbor)
                        queue.append(neighbor)
    return cluster

def flipSpins(ising, cluster):
    return ising



if __name__ == '__main__':
    import matplotlib.pyplot as plt
    N = 20
    ising = initializeIsing(N)
    Js = initializeJ(N)
    fig, axes = plt.subplots(2, figsize = (6,6))
    axes[0].imshow(ising)
    ising = wolffFlip(ising, Js, 0)
    axes[1].imshow(ising)
    plt.show()