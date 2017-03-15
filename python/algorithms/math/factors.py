import unittest


def all_factors(number):
    factors = []

    sqrt_n = number ** 0.5

    for i in range(1, int(sqrt_n)+1):
        if number % i == 0:
            factors.append(i)

            if i != sqrt_n:
                factors.append(number//i)

    return sorted(factors)


class TestAllFactors(unittest.TestCase):

    def test_test1(self):
        expected_result = [1]

        actual_result = all_factors(1)

        self.assertEqual(actual_result, expected_result)

    def test_test12(self):
        # sqrt = 3.46
        expected_result = [1, 2, 3, 4, 6, 12]

        actual_result = all_factors(12)

        self.assertEqual(actual_result, expected_result)

    def test_test14(self):
        # sqrt = 3.74
        expected_result = [1, 2, 7, 14]

        actual_result = all_factors(14)

        self.assertEqual(actual_result, expected_result)

    def test_test16(self):
        # sqrt = 4
        expected_result = [1, 2, 4, 8, 16]

        actual_result = all_factors(16)

        self.assertEqual(actual_result, expected_result)

    def test_test38808(self):

        # sqrt = 196.99746
        expected_result = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 14, 18, 21, 22, 24, 28, 33, 36, 42, 44, 49, 56, 63,
                           66, 72, 77, 84, 88, 98, 99, 126, 132, 147, 154, 168, 196, 198, 231, 252, 264, 294,
                           308, 392, 396, 441, 462, 504, 539, 588, 616, 693, 792, 882, 924, 1078, 1176, 1386,
                           1617, 1764, 1848, 2156, 2772, 3234, 3528, 4312, 4851, 5544, 6468, 9702, 12936,
                           19404, 38808]

        actual_result = all_factors(38808)

        self.assertEqual(actual_result, expected_result)

