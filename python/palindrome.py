import unittest


def is_palindrome(astring):
    for i in range(len(astring) // 2):
        if astring[i] != astring[len(astring)-i-1]:
            return False
    return True


def is_palindrome_with_punctuation(a_string):
    i = 0
    j = len(a_string) - 1
    while i < j:
        while (not a_string[i].isalpha() or not a_string[j].isalpha()) and i < j:
            if not a_string[i].isalpha():
                i += 1
            if not a_string[j].isalpha():
                j -= 1
        if a_string[i] != a_string[j]:
            return False
        i += 1
        j -= 1

    return True

if __name__ == '__main__':
    str4 = '.;abc----z;c-b.a.'
    print is_palindrome_with_punctuation(str4)


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


class TestPalindromesWithPunctuation(unittest.TestCase):

    def test_palindromes(self):
        test_string = ''
        self.assertTrue(is_palindrome_with_punctuation(test_string))

        test_string = ';-,'
        self.assertTrue(is_palindrome_with_punctuation(test_string))

        test_string = '--.x-,'
        self.assertTrue(is_palindrome_with_punctuation(test_string))

        test_string = '..a-a....'
        self.assertTrue(is_palindrome_with_punctuation(test_string))

        test_string = 'a,b,,c,,,d,e.e/d/c/b;;a'
        self.assertTrue(is_palindrome_with_punctuation(test_string))

        test_string = '.a--b/c;d;e..x.e/d//c.b;;;a;;;-.'
        self.assertTrue(is_palindrome_with_punctuation(test_string))

    def test_not_palindromes(self):
        test_string = '.a.y.....'
        self.assertFalse(is_palindrome_with_punctuation(test_string))

        test_string = '.a/b;c;d;e;e,,d,c,,,,b...y...;'
        self.assertFalse(is_palindrome_with_punctuation(test_string))

        test_string = 'abcdexedcbay'
        self.assertFalse(is_palindrome_with_punctuation(test_string))
