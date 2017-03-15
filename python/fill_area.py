import unittest


def calculate_valid_neighbors(pos, current_board, max_x, max_y):

    moves = [
        (0, -1), (0, 1), (-1, 0), (1, 0)
    ]

    valid_neighbors = []
    for move in moves:
        new_x = pos[0] + move[0]
        new_y = pos[1] + move[1]

        # board elements should be indexed board[y][x]
        if (0 <= new_x <= max_x) and (0 <= new_y <= max_y)\
                and current_board[new_y][new_x] != 'X':
            valid_neighbors.append((new_x, new_y))

    return valid_neighbors


def fill_area(board, x, y):

    max_x = len(board[0]) - 1
    max_y = len(board) - 1

    # print max_x, max_y

    if x > max_x or y > max_y:
        return board

    x_indexes = [str(i) for i in range(len(board[0]))]

    current_board = board
    start_pos = (x, y)
    stack = [start_pos]
    while stack:
        print 'stack:', stack
        pos = stack.pop()
        print 'processing pos', pos
        # board elements should be indexed board[y][x]
        current_board[pos[1]][pos[0]] = 'X'
        print ' ', x_indexes
        for y_index, row in enumerate(current_board):
            print y_index, row
        valid_neighbors = calculate_valid_neighbors(pos, current_board, max_x, max_y)
        print 'valid_neighbors:', valid_neighbors
        for neighbor in valid_neighbors:
            if neighbor not in stack:
                stack.append(neighbor)

    return board


class TestFillArea(unittest.TestCase):

    def test_x_y_out_of_bound(self):
        board = [
            ['X', 'X', 'X', '.', '.', '.'],
            ['X', '.', '.', 'X', '.', '.'],
            ['X', 'X', '.', '.', 'X', '.'],
            ['.', 'X', '.', '.', 'X', '.'],
            ['.', 'X', '.', 'X', '.', '.'],
            ['.', '.', 'X', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
        ]

        expected_board = board

        actual_board = fill_area(board, 10, 10)
        self.assertEqual(actual_board, expected_board)

    def test_simple1(self):
        board = [
            ['.', 'X', 'X', 'X', 'X', '.'],
            ['.', 'X', '.', '.', 'X', '.'],
            ['.', 'X', '.', '.', 'X', '.'],
            ['.', 'X', '.', '.', 'X', '.'],
            ['.', 'X', 'X', 'X', 'X', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
        ]

        expected_board = [
            ['.', 'X', 'X', 'X', 'X', '.'],
            ['.', 'X', 'X', 'X', 'X', '.'],
            ['.', 'X', 'X', 'X', 'X', '.'],
            ['.', 'X', 'X', 'X', 'X', '.'],
            ['.', 'X', 'X', 'X', 'X', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
        ]

        actual_board = fill_area(board, 2, 2)
        self.assertEqual(actual_board, expected_board)

    def test_board2(self):

        board = [
            ['X', 'X', 'X', '.', '.', '.'],
            ['X', '.', '.', 'X', '.', '.'],
            ['X', 'X', '.', '.', 'X', '.'],
            ['.', 'X', '.', '.', 'X', '.'],
            ['.', 'X', '.', 'X', '.', '.'],
            ['.', '.', 'X', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
        ]

        expected_board = [
            ['X', 'X', 'X', '.', '.', '.'],
            ['X', 'X', 'X', 'X', '.', '.'],
            ['X', 'X', 'X', 'X', 'X', '.'],
            ['.', 'X', 'X', 'X', 'X', '.'],
            ['.', 'X', 'X', 'X', '.', '.'],
            ['.', '.', 'X', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
        ]

        actual_board = fill_area(board, 2, 2)
        self.assertEqual(actual_board, expected_board)
