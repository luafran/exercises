import unittest


def is_palindrome(astring):
    for i in range(len(astring) // 2):
        if astring[i] != astring[len(astring)-i-1]:
            return False
    return True


class TestPalindromes(unittest.TestCase):

    def test_palindromes(self):
        test_string = ''
        self.assertTrue(is_palindrome(test_string))

        test_string = 'x'
        self.assertTrue(is_palindrome(test_string))

        test_string = 'aa'
        self.assertTrue(is_palindrome(test_string))

        test_string = 'abcdeedcba'
        self.assertTrue(is_palindrome(test_string))

        test_string = 'abcdexedcba'
        self.assertTrue(is_palindrome(test_string))

    def test_not_palindromes(self):
        test_string = 'ay'
        self.assertFalse(is_palindrome(test_string))

        test_string = 'abcdeedcby'
        self.assertFalse(is_palindrome(test_string))

        test_string = 'abcdexedcbay'
        self.assertFalse(is_palindrome(test_string))
