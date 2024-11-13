import wolff    # The code to test
import init
import unittest 
import numpy as np

class Test_Ising(unittest.TestCase):
    
    def test_addToCluster100p(self):
        ising = [
            [-1, -1],
            [1, -1],
        ]
        Js = init.initializeJ(3)
        inPoint = (0, 1)
        targetPoint = (1, 1)
        i = 2
        self.assertTrue(wolff.addToCluster100percent(ising, targetPoint, inPoint, i, Js))

    def test_addToCluster100p2(self):
        ising = [
            [-1, -1],
            [1, -1],
        ]
        Js = init.initializeJ(3)
        inPoint = (0, 0)
        targetPoint = (1, 0)
        i = 2
        self.assertFalse(wolff.addToCluster100percent(ising, targetPoint, inPoint, i, Js))

    def test_addToCluster100p3(self):
        ising = [
            [-1, -1],
            [1, -1],
        ]
        Js = init.initializeJ(3, "-1")
        inPoint = (0, 0)
        targetPoint = (1, 0)
        i = 2
        self.assertTrue(wolff.addToCluster100percent(ising, targetPoint, inPoint, i, Js))

    def test_addToCluster100p4(self):
        ising = [
            [-1, -1],
            [1, -1],
        ]
        Js = init.initializeJ(3, "-1")
        inPoint = (0, 1)
        targetPoint = (1, 1)
        i = 2
        self.assertFalse(wolff.addToCluster100percent(ising, targetPoint, inPoint, i, Js))

    def test_addToCluster_1(self):
        ising = [
            [-1, -1],
            [1, -1],
        ]
        temp = np.inf
        Js = init.initializeJ(3, "-1")
        i = 2
        inPoint = (0, 1)
        targetPoint = (1, 1)
        self.assertFalse(wolff.addToCluster(ising, targetPoint, inPoint, i, Js, temp))
        inPoint = (0, 0)
        targetPoint = (1, 0)
        self.assertFalse(wolff.addToCluster(ising, targetPoint, inPoint, i, Js, temp))

    def test_addToCluster_2(self):
        ising = [
            [-1, -1],
            [1, -1],
        ]
        temp = 0
        Js = init.initializeJ(3, "-1")
        i = 2
        inPoint = (0, 1)
        targetPoint = (1, 1)
        self.assertFalse(wolff.addToCluster(ising, targetPoint, inPoint, i, Js, temp))
        inPoint = (0, 0)
        targetPoint = (1, 0)
        self.assertTrue(wolff.addToCluster(ising, targetPoint, inPoint, i, Js, temp))

    def test_wolff_clustering1(self):
        N = 3
        ising = [
            [-1, 1, -1],
            [1, -1, 1],
            [-1, 1, -1]
        ]
        Js = init.initializeJ(3)
        cluster = wolff.findCluster(ising, Js, 10)
        self.assertEqual(1, len(cluster))

    def test_wolff_clustering2(self):
        N = 3
        ising = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        Js = init.initializeJ(3)
        cluster = wolff.findCluster(ising, Js, 0)
        self.assertEqual(9, len(cluster))

    def test_wolff_clustering3(self):
        N = 3
        ising = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        Js = init.initializeJ(3)
        cluster = wolff.findCluster(ising, Js, np.inf)
        self.assertEqual(1, len(cluster))

    def test_wolff_clustering4(self):
        N = 4
        ising = [
            [1, 1, -1, -1],
            [1, 1, -1, -1],
            [1, 1, -1, -1],
            [1, 1, -1, -1]
        ]
        Js = init.initializeJ(N)
        cluster = wolff.findCluster(ising, Js, 0)
        self.assertEqual(8, len(cluster))


           












if __name__ == '__main__':
    unittest.main()