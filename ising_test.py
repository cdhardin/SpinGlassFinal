import ising    # The code to test
import unittest 
import numpy as np

class Test_Ising(unittest.TestCase):


   def test_spinSetup(self):
      N = 100
      spins = ising.initializeIsing(N)
      sum = np.sum(np.abs(spins))
      self.assertEqual(sum, N * N)

   def test_J_ones(self):
      N = 100
      Js = ising.initializeJ(N, "Ones")
      sum0 = np.sum(Js[0])
      sum1 = np.sum(Js[1])
      self.assertEqual(sum0, sum1)
      self.assertEqual(sum1, N * (N))

   def test_J_pm(self):
      N = 100
      Js = ising.initializeJ(N, "pm")
      sum0 = np.sum(Js[0])
      sum1 = np.sum(Js[1])
      sum2 = np.sum(np.abs(Js[1]))
      self.assertFalse(sum0 == N * (N))
      self.assertFalse(sum1 == N * (N))
      self.assertTrue(sum2 == N * (N))

   def test_energy_calc_allPos(self):
      N = 37
      spins = np.abs(ising.initializeIsing(N))
      Js = ising.initializeJ(N, "Ones")
      expectedE = - (2*N*(N-1))
      E = ising.calculateEnergy(spins, Js)
      print(f"expect: {expectedE}, got {E}")
      self.assertEqual(expectedE, E)
      
   def test_energy_calc_allPos(self):
      N = 37
      spins = np.abs(ising.initializeIsing(N))
      Js = ising.initializeJ(N, "Ones")
      expectedE = - (2*N*(N))
      E = ising.calculateEnergy(spins, Js)
      self.assertEqual(expectedE, E)

   def test_singleFlip(self):
      N = 38
      I = ising.initializeIsing(N)
      a = ising.flipSingleSpin(I, (4,5))
      print((I != a))
      self.assertEqual(np.sum(I != a), 1)



   def test_get_neighbors1(self):
      N = 10
      ising1 = np.zeros((N,N))
      spot = (5,5)
      neighborList = [(5,6), (5,4), (6,5), (4,5)]
      funcNeighbors = ising.getNeighbors(ising1, spot)
      for i in range(4):
         self.assertEqual(neighborList[i], funcNeighbors[i])

   def test_get_neighbors2(self):
      N = 3
      ising1 = np.zeros((N,N))
      spot = (0,1)
      neighborList = [(0,2), (0,0), (1,1), (2,1)]
      funcNeighbors = ising.getNeighbors(ising1, spot)
      for i in range(4):
         self.assertEqual(neighborList[i], funcNeighbors[i])

   def test_getJfromNum_1(self):
      N = 5
      J_down = np.random.random((5,5))
      J_right = np.random.random((5,5))
      J_arr = (J_down, J_right)
      spot = (3,3)
      Js_cycle = [J_right[3,3], J_right[3,2], J_down[3,3], J_down[2,3]]
      for i in range(4):
         print(i)
         self.assertEqual(Js_cycle[i], ising.getJfromNum(i, spot, J_arr))

   def test_getJfromNum_2(self):
      N = 5
      J_down = np.random.random((5,5))
      J_right = np.random.random((5,5))
      J_arr = (J_down, J_right)
      spot = (0,3)
      Js_cycle = [J_right[0,3], J_right[0,2], J_down[0,3], 0]
      for i in range(4):
         self.assertEqual(Js_cycle[i], ising.getJfromNum(i, spot, J_arr))










if __name__ == '__main__':
    unittest.main()