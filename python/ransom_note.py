import unittest
from collections import Counter


def ransom_note(magazine, ransom):
    print '#' * 5

    if len(magazine) < len(ransom):
        return False

    c_magazine = Counter(magazine)
    c_ransom = Counter(ransom)

    c_magazine.subtract(c_ransom)

    for count in c_magazine.values():
        print count
        if count < 0:
            return False

    return True

if __name__ == '__main__':
    m, n = map(int, raw_input().strip().split(' '))
    mag = raw_input().strip().split(' ')
    ran = raw_input().strip().split(' ')

    ans = ransom_note(mag, ran)
    if ans:
        print "Yes"
    else:
        print "No"


class TestRansomNote(unittest.TestCase):

    def test_example(self):
        magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
        ransom = ['give', 'one', 'grand', 'today']

        answer = ransom_note(magazine, ransom)

        self.assertTrue(answer)

    def test_exact(self):
        magazine = ['give', 'one', 'grand', 'today']
        ransom = ['give', 'one', 'grand', 'today']

        answer = ransom_note(magazine, ransom)

        self.assertTrue(answer)

    def test_less(self):
        magazine = ['give', 'one', 'grand', 'today']
        ransom = ['give', 'me', 'one', 'grand', 'today', 'night']

        answer = ransom_note(magazine, ransom)

        self.assertFalse(answer)

    def test_no_1(self):
        magazine = ['give', 'one', 'grand', 'today', 'day', 'tomorrow']
        ransom = ['give', 'me', 'one', 'grand', 'today', 'night']

        answer = ransom_note(magazine, ransom)

        self.assertFalse(answer)

    def test_no_2(self):
        magazine = ['give', 'me', 'one', 'grand', 'today', 'day', 'tomorrow']
        ransom = ['give', 'me', 'one', 'grand', 'today', 'today']

        answer = ransom_note(magazine, ransom)

        self.assertFalse(answer)

    def test_yes_1(self):
        magazine = ['give', 'me', 'one', 'grand', 'today', 'today', 'tomorrow']
        ransom = ['give', 'me', 'one', 'grand', 'today', 'today']

        answer = ransom_note(magazine, ransom)

        self.assertTrue(answer)
