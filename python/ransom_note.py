# coding=utf-8
import unittest
from collections import Counter
from collections import defaultdict


def ransom_note_dicts(magazine, ransom_note):
    words = defaultdict(int)
    for word in ransom_note:
        words[word] += 1

    for word in magazine:
        if word in words:
            words[word] -= 1
            if words[word] == 0:
                del words[word]

    return len(words) == 0


def ransom_note_counters(magazine, ransom_note):
    print('#' * 5)

    if len(magazine) < len(ransom_note):
        return False

    c_ransom_note = Counter(ransom_note)
    c_magazine = Counter(magazine)

    c_ransom_note.subtract(c_magazine)

    for count in c_ransom_note.values():
        print('count', count)
        if count > 0:
            return False

    return True


if __name__ == '__main__':
    m, n = map(int, input().strip().split(' '))
    mag = input().strip().split(' ')
    ran = input().strip().split(' ')

    ans = ransom_note_counters(mag, ran)
    if ans:
        print("Yes")
    else:
        print("No")


class TestRansomNote(unittest.TestCase):

    def test_example(self):
        magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
        ransom = ['give', 'one', 'grand', 'today']

        answer = ransom_note_counters(magazine, ransom)
        self.assertTrue(answer)

        answer2 = ransom_note_dicts(magazine, ransom)
        self.assertTrue(answer2)

    def test_exact(self):
        magazine = ['give', 'one', 'grand', 'today']
        ransom = ['give', 'one', 'grand', 'today']

        answer = ransom_note_counters(magazine, ransom)
        self.assertTrue(answer)

        answer2 = ransom_note_dicts(magazine, ransom)
        self.assertTrue(answer2)

    def test_less(self):
        magazine = ['give', 'one', 'grand', 'today']
        ransom = ['give', 'me', 'one', 'grand', 'today', 'night']

        answer = ransom_note_counters(magazine, ransom)
        self.assertFalse(answer)

        answer2 = ransom_note_dicts(magazine, ransom)
        self.assertFalse(answer2)

    def test_no_1(self):
        magazine = ['give', 'one', 'grand', 'today', 'day', 'tomorrow']
        ransom = ['give', 'me', 'one', 'grand', 'today', 'night']

        answer = ransom_note_counters(magazine, ransom)
        self.assertFalse(answer)

        answer2 = ransom_note_dicts(magazine, ransom)
        self.assertFalse(answer2)

    def test_no_2(self):
        magazine = ['give', 'me', 'one', 'grand', 'today', 'day', 'tomorrow']
        ransom = ['give', 'me', 'one', 'grand', 'today', 'today']

        answer = ransom_note_counters(magazine, ransom)
        self.assertFalse(answer)

        answer2 = ransom_note_dicts(magazine, ransom)
        self.assertFalse(answer2)

    def test_yes_1(self):
        magazine = ['give', 'me', 'one', 'grand', 'today', 'today', 'tomorrow']
        ransom = ['give', 'me', 'one', 'grand', 'today', 'today']

        answer = ransom_note_counters(magazine, ransom)
        self.assertTrue(answer)

        answer2 = ransom_note_dicts(magazine, ransom)
        self.assertTrue(answer2)
