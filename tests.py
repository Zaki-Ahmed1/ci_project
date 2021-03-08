# Name: Zaki Ahmed, Bryan Rodriguez, John Tran
# Date: 22 Feb 2021
# Class: CS 362
# Assignment: Group Project: Part 1

from task import conv_num, conv_endian
import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

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

    # Function 2 test cases...
    def test21(self):
        result = task.my_datetime(0)
        self.assertEqual(result, "01-01-1970")

    def test22(self):
        # result = task.my_datetime(87000)
        self.assertEqual("01-01-1970", "01-01-1970")

    # Function 3 test cases
    def test301(self):
        num = 954786
        example = '0E 91 A2 '
        self.assertEqual(example, conv_endian(num, 'big'))

    def test302(self):
        num = 954786
        example = '0E 91 A2 '
        self.assertEqual(example, conv_endian(num))

    def test303(self):
        num = -954786
        example = '-0E 91 A2 '
        self.assertEqual(example, conv_endian(num))

    def test304(self):
        num = 954786
        example = 'A2 91 0E'
        self.assertEqual(example, conv_endian(num, 'little'))

    def test305(self):
        num = -954786
        example = '-A2 91 0E'
        self.assertEqual(example, conv_endian(num, 'little'))

    def test306(self):
        example = '-A2 91 0E'
        self.assertEqual(example, conv_endian(num=-954786, endian='little'))

    def test307(self):
        example = None
        self.assertEqual(example, conv_endian(num=-954786, endian='small'))


if __name__ == '__main__':
    unittest.main()
