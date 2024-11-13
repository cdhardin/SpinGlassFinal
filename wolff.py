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
    return ising

#pickRandomSpot(ising) to pick starting spot

def addToCluster(ising, neighbor, spot):
    #Return True or False depending on if we're gonna add point to the cluster
    return 

def findCluster(ising, Js, temp):
    initialSpot = findCluster(ising)
    visitedPoints = {initialSpot}
    queue = [initialSpot]
    cluster = [initialSpot]
    while len(queue) > 0:
        spot = queue.pop(0)
        neighbors = getNeighbors(ising, spot)
        for neighbor in neighbors:
            if neighbor in visitedPoints:
                continue
            else:
                visitedPoints.add(neighbor)
                if addToCluster(neighbor, spot):
                    cluster.append(neighbor)
                    queue.append(neighbor)
    
    return cluster

def flipSpins(ising, cluster):
    return ising