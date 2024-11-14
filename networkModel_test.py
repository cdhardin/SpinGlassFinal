import networkModel as nm    # The code to test
import init
import unittest 
import numpy as np

class Test_Network(unittest.TestCase):
    def test1(self):
        self.assertTrue(1)
    
    def testBinaryConvert6(self):
        N = 6
        Nbin = "110"
        num, ind = nm.find_indices_of_ones(N)
        self.assertEqual(Nbin, num)
        print(ind)
        self.assertEqual([1,2], ind)
        self.assertEqual(nm.binToInt(num), N)
    
    def testBinaryConvert1(self):
        N = 1
        Nbin = "1"
        num, ind = nm.find_indices_of_ones(N)
        self.assertEqual(Nbin, num)
        print(ind)
        self.assertEqual([0], ind)
        self.assertEqual(nm.binToInt(num), N)
    
    def testBinaryConvert0(self):
        N = 0
        Nbin = "0"
        num, ind = nm.find_indices_of_ones(N)
        self.assertEqual(Nbin, num)
        print(ind)
        self.assertEqual([], ind)
        self.assertEqual(nm.binToInt(num), N)
    
    def testBinaryConvert7(self):
        N = 7
        Nbin = "111"
        num, ind = nm.find_indices_of_ones(N)
        self.assertEqual(Nbin, num)
        print(ind)
        self.assertEqual([0,1,2], ind)
        self.assertEqual(nm.binToInt(num), N)


if __name__ == '__main__':
    unittest.main()