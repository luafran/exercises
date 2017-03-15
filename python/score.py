import unittest


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def total_score(blocks, n):

    scores = []
    for symbol in blocks:
        if not isinstance(symbol, str):
            continue
        if is_number(symbol):
            scores.append(int(symbol))
        elif symbol == 'Z':
            try:
                scores.pop()
            except IndexError:
                pass
        elif symbol == 'X':
            last = scores[len(scores)-1]
            scores.append(last*2)
        elif symbol == '+':
            print 'len:', len(scores)
            last1 = scores[len(scores) - 1] if len(scores) > 0 else 0
            last2 = scores[len(scores) - 2] if len(scores) > 0 else 0
            print last1, last2
            scores.append(last1+last2)

    result = sum(scores)
    print result
    return result


class TestTotalScore(unittest.TestCase):

    def test_test1(self):
        blocks = ['5', '-2', '4', 'Z', 'X', '9', '+', '+']
        n = 8

        result = total_score(blocks, n)

        self.assertEqual(result, 27)

    def test_test2(self):
        blocks = ['1', '2', '+', 'Z']
        n = 4

        result = total_score(blocks, n)

        self.assertEqual(result, 3)

    def test_test3(self):
        blocks = ['Z', '2', '+', 'Z']
        n = 4

        result = total_score(blocks, n)

        self.assertEqual(result, 2)

    def test_test4(self):
        blocks = ['+', '2', '+', 'Z']
        n = 4

        result = total_score(blocks, n)

        self.assertEqual(result, 2)
