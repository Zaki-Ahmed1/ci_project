# Name: Zaki Ahmed, Bryan Rodriguez, John Tran
# Date: 22 Feb 2021
# Class: CS 362
# Assignment: Grou Project: Part 1


import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)
    

    # Function 2 test cases...
    def test21(self):
        result = task.my_datetime(0)
        self.assertEqual(result, "01-01-1970")

if __name__ == '__main__':
    unittest.main()
