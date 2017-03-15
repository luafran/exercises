import unittest


def decimal_to_base(decimal_number, base):

    binary = []

    rem, quotient = divmod(decimal_number, base)
    binary.append(quotient)
    decimal_number = rem
    while rem != 0:
        rem, quotient = divmod(decimal_number, base)
        binary.append(quotient)
        decimal_number = rem

    return ''.join(str(digit) for digit in reversed(binary))


DEC_TO_HEX_SINGLE_DIGIT = "0123456789ABCDEF"


def to_hex(n):  # 0 < n < 16
    return DEC_TO_HEX_SINGLE_DIGIT[n]


def decimal_to_hex(n):
    if n < 16:
        return to_hex(n)
    mod = n % 16
    n /= 16
    return decimal_to_hex(n) + str(to_hex(mod))


class TestDecimalToBinary(unittest.TestCase):

    def test_0(self):

        self.assertEqual('0', decimal_to_base(0, 2))

    def test_6(self):
        self.assertEqual('110', decimal_to_base(6, 2))

    def test_27(self):
        self.assertEqual('11011', decimal_to_base(27, 2))


class TestDecimalToOctal(unittest.TestCase):

    def test_0(self):

        self.assertEqual('0', decimal_to_base(0, 8))

    def test_9(self):
        self.assertEqual('11', decimal_to_base(9, 8))

    def test_27(self):
        self.assertEqual('33', decimal_to_base(27, 8))


class TestDecimalToHexadecimal(unittest.TestCase):

    def test_0(self):

        self.assertEqual('0', decimal_to_hex(0))

    def test_10(self):
        self.assertEqual('A', decimal_to_hex(10))

    def test_254(self):
        self.assertEqual('FE', decimal_to_hex(254))
