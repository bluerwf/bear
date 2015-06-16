#! /usr/bin/env python
# coding=utf-8
import unittest
from mystr import find_upper, find_upper2

class Teststring(unittest.TestCase):
    def setUp(self):
       self.demo_str = "I am Gay"

    def test_find_upper(self):
        a = 'I am Gay'
        upper  = find_upper(a)
        self.assertListEqual(upper,['I', 'G'])

        self.assertEqual(upper[0], 'I')
     
    def test_find_upper2(self):
        a = 'I am Les'
        upper = find_upper2(a)
        self.assertListEqual(upper, ['I','L'])
