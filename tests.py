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

    def test111(self):
        string = "-0x."
        output = None
        self.assertEqual(output, conv_num(string))

    def test112(self):
        string = "-"
        output = None
        self.assertEqual(output, conv_num(string))

    def test113(self):
        string = "."
        output = 0.0
        self.assertEqual(output, conv_num(string))

    def test114(self):
        string = "12-34"
        output = None
        self.assertEqual(output, conv_num(string))

    def test115(self):
        string = 1234
        output = None
        self.assertEqual(output, conv_num(string))

    def test116(self):
        string = "12*34"
        output = None
        self.assertEqual(output, conv_num(string))

    # Function 2 test cases...
    def test201(self):
        result = task.my_datetime(0)
        self.assertEqual(result, "01-01-1970")

    def test202(self):
        result = task.my_datetime(123456789)
        self.assertEqual(result, "11-29-1973")

    def test203(self):
        result = task.my_datetime(9876543210)
        self.assertEqual(result, "12-22-2282")

    def test204(self):
        result = task.my_datetime(201653971200)
        self.assertEqual(result, "02-29-8360")

    def test205(self):
        result = task.my_datetime(86399)
        self.assertEqual(result, "01-01-1970")

    def test206(self):
        result = task.my_datetime(86400)
        self.assertEqual(result, "01-02-1970")

    def test207(self):
        result = task.my_datetime(86401)
        self.assertEqual(result, "01-02-1970")

    def test208(self):
        result = task.my_datetime(86400 * 2)
        self.assertEqual(result, "01-03-1970")

    # Function 3 test cases
    def test301(self):
        num = 954786
        example = '0E 91 A2'
        self.assertEqual(example, conv_endian(num, 'big'))

    def test302(self):
        num = 954786
        example = '0E 91 A2'
        self.assertEqual(example, conv_endian(num))

    def test303(self):
        num = -954786
        example = '-0E 91 A2'
        self.assertEqual(example, conv_endian(num))

    def test304(self):
        num = -95
        example = '-5F'
        self.assertEqual(example, conv_endian(num))

    def test305(self):
        num = 954786
        example = 'A2 91 0E'
        self.assertEqual(example, conv_endian(num, 'little'))

    def test306(self):
        num = -954786
        example = '-A2 91 0E'
        self.assertEqual(example, conv_endian(num, 'little'))

    def test307(self):
        example = '-A2 91 0E'
        self.assertEqual(example, conv_endian(num=-954786, endian='little'))

    def test308(self):
        example = None
        self.assertEqual(example, conv_endian(num=-954786, endian='small'))

    def test309(self):
        num = 954786
        example = None
        self.assertEqual(example, conv_endian(num, endian=''))

    def test310(self):
        num = 954786
        example = None
        self.assertEqual(example, conv_endian(num, 'icecream'))

    def test311(self):
        num = 1
        example = '01'
        self.assertEqual(example, conv_endian(num, 'big'))

    def test312(self):
        num = 1
        example = '01'
        self.assertEqual(example, conv_endian(num, 'little'))

    def test313(self):
        num = 1
        example = None
        self.assertEqual(example, conv_endian(num, 'bigfish'))

    def test314(self):
        num = 1
        example = None
        self.assertEqual(example, conv_endian(num, 'littlefish'))

    def test315(self):
        num = -1
        example = '-01'
        self.assertEqual(example, conv_endian(num, 'big'))

    def test316(self):
        num = -1
        example = '-01'
        self.assertEqual(example, conv_endian(num, 'little'))

    def test317(self):
        num = -1
        example = None
        self.assertEqual(example, conv_endian(num, 'bigfish'))

    def test318(self):
        num = -1
        example = None
        self.assertEqual(example, conv_endian(num, 'littlefish'))

    def test319(self):
        num = 95
        example = '5F'
        self.assertEqual(example, conv_endian(num))


if __name__ == '__main__':
    unittest.main()
