import unittest
from sort import Sort

class TestSort(unittest.TestCase):
    def setUp(self):
        self.sorter = Sort()

    def test_bubble(self):
        a =[9,1,7,6,5,4,3,2]
        self.assertListEqual(self.sorter.bubble(a), [1,2,3,4,5,6,7,9])

    def test_qsort(self):
        a=[6,5,7,9,8]
        self.sorter.qsort(0, len(a) - 1, a)
        self.assertListEqual(a, [5,6,7,8,9])

