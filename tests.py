# Name: Zaki Ahmed, Bryan Rodriguez, John Tran
# Date: 22 Feb 2021
# Class: CS 362
# Assignment: Group Project: Part 1


from task import conv_num
import unittest


class TestCase(unittest.TestCase):

    def test100(self):
        string = "12345"
        output = 12345
        self.assertEqual(output, conv_num(string))

    def test101(self):
        string = "-123.45"
        output = -123.45
        self.assertEqual(output, conv_num(string))

    def test102(self):
        string = ".45"
        output = 0.45
        self.assertEqual(output, conv_num(string))

    def test103(self):
        string = "123."
        output = 123.0
        self.assertEqual(output, conv_num(string))

    def test104(self):
        string = "0xAD4"
        output = 2772
        self.assertEqual(output, conv_num(string))

    def test105(self):
        string = "0xAZ4"
        output = None
        self.assertEqual(output, conv_num(string))

    def test106(self):
        string = "12345A"
        output = None
        self.assertEqual(output, conv_num(string))

    def test107(self):
        string = "12.3.45"
        output = None
        self.assertEqual(output, conv_num(string))
    
    def test108(self):
        string = "100000000000000"
        output = 100000000000000
        self.assertEqual(output, conv_num(string))

    def test109(self):
        string = ""
        output = None
        self.assertEqual(output, conv_num(string))
    
    def test110(self):
        string = "     "
        output = None
        self.assertEqual(output, conv_num(string))
    

if __name__ == '__main__':
    unittest.main()
