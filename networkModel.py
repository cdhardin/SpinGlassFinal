import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

from init import *
from wolff import *
from single_flip import *

## Network Idea, not pursuing for now

N = 2

def find_indices_of_ones(n):
    # Convert integer to binary string (removing the '0b' prefix)
    binary_representation = bin(n)[2:]
    
    # Find indices of '1's (counting from the right)
    indices = [i for i, bit in enumerate(reversed(binary_representation)) if bit == '1']
    
    return binary_representation, indices

def binToInt(binary_string):
    number = int(binary_string, 2)
    return number

def buildSpecificIsing(N, num):
    emptyIsing = np.ones((N, N))
    _, spinInts = find_indices_of_ones(num)
    for spin in range(N*N):
        if spin in spinInts:
            # print(f"num - {num}, spin - {spin}")
            i = spin % N
            j = int(spin / N)
            emptyIsing[i][j] = -1
    return emptyIsing

def makeAdjMat(N):
    totNum = N*N
    graphMatrix = np.zeros((totNum, totNum))


    
if __name__ == '__main__':
    N = 3
   


    for i in range(2**(N*N)):
        plt.imshow(buildSpecificIsing(N,i))
        plt.show()



