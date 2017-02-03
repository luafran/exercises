import unittest


def total_score(blocks, n):
    score = []
    for symbol in blocks:
        print symbol
        if isinstance(symbol, int):
            score.append(symbol)
        elif isinstance(symbol, str):
            if symbol == 'Z':
                score.pop()
            elif symbol == 'X':
                last = score[len(score)-1]
                score.append(last*2)
            elif symbol == '+':
                last2 = score[len(score) - 2]
                last1 = score[len(score) - 1]
                score.append(last1+last2)
        print score
    result = sum(score)

    return result


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def totalScore(blocks, n):

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

        result = totalScore(blocks, n)

        self.assertEqual(result, 27)

    def test_test2(self):
        blocks = ['1', '2', '+', 'Z']
        n = 4

        result = totalScore(blocks, n)

        self.assertEqual(result, 3)

    def test_test3(self):
        blocks = ['Z', '2', '+', 'Z']
        n = 4

        result = totalScore(blocks, n)

        self.assertEqual(result, 2)

    def test_test4(self):
        blocks = ['+', '2', '+', 'Z']
        n = 4

        result = totalScore(blocks, n)

        self.assertEqual(result, 2)
