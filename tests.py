# Name: Zaki Ahmed, Bryan Rodriguez, John Tran
# Date: 22 Feb 2021
# Class: CS 362
# Assignment: Grou Project: Part 1


from task import conv_num
import unittest


class TestCase(unittest.TestCase):

    def test100(self):
        string = "12345"
        output = 12345
        self.assertEqual(output, conv_num(string))
    
    # def test101(self):
    #     string = "-123.45"
    #     output = -123.45
    #     self.assertEqual(output, conv_num(string))

    # def conv_num_test1(self):
    #     self.assertTrue(True)
    
    # def conv_num_test1(self):
    #     self.assertTrue(True)
    
    # def conv_num_test1(self):
    #     self.assertTrue(True)
    
    # def conv_num_test1(self):
    #     self.assertTrue(True)
    
    # def conv_num_test1(self):
    #     self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
