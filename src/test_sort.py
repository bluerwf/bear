import unittest
from sort import Sort

class TestSort(unittest.TestCase):
    def setUp(self):
        self.sorter = Sort()

    def test_bubble(self):
        a =[9,1,7,6,5,4,3,2]
        b = []
        self.assertListEqual(self.sorter.bubble(a), [1,2,3,4,5,6,7,9])
        self.assertListEqual(self.sorter.bubble(b), [])
