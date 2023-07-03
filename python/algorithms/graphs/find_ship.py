# Python 3.8
from typing import List
from collections import deque
import unittest


class FindBattleShips:
    SHIP = 'X'
    WATER = '.'

    def __init__(self, battle_field: List[List[str]]):
        self.battle_field = battle_field
        self.rows_num = len(battle_field)
        if self.rows_num > 0:
            self.cols_num = len(battle_field[0])
        else:
            self.cols_num = 0
        # print('rows_num:', self.rows_num, 'cols_num:', self.cols_num)

    def is_valid(self, row, col):
        return 0 <= row < self.rows_num and 0 <= col < self.cols_num and self.battle_field[row][col] == self.SHIP

    def sink_ship(self, i, j):
        dir_row = [0, 1, 0, -1]
        dir_col = [-1, 0, 1, 0]

        ship_coordinates = []
        frontier = deque()
        frontier.appendleft((i, j))
        while frontier:
            row, col = frontier.popleft()
            # print('processing', row, col)
            if not self.is_valid(row, col):
                continue

            # print('sinking:', row, col)
            ship_coordinates.append([row, col])
            self.battle_field[row][col] = self.WATER

            for k in range(4):
                adj_x = row + dir_row[k]
                adj_y = col + dir_col[k]
                # print('adding', adj_x, adj_y, 'to frontier')
                frontier.appendleft((adj_x, adj_y))

        return ship_coordinates

    def find_battle_ships(self) -> int:
        ships_found = 0
        if self.rows_num < 1:
            return ships_found

        for i in range(self.rows_num):
            for j in range(self.cols_num):
                if self.is_valid(i, j):
                    print('found ship at:', i, j)
                    ship_coordinates = self.sink_ship(i, j)
                    print('ship coordinates:', ship_coordinates)
                    ships_found += 1

        return ships_found


class TestsFindBattleShips(unittest.TestCase):

    def test_empty(self):
        battle_field = []
        c = FindBattleShips(battle_field)
        battle_ships = c.find_battle_ships()
        self.assertEqual(0, battle_ships)

    def test_no_ship(self):
        battle_field = [
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
        ]
        c = FindBattleShips(battle_field)
        battle_ships = c.find_battle_ships()
        self.assertEqual(0, battle_ships)

    def test_one_ship_top_left_h(self):
        battle_field = [
            ['X', 'X', 'X', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
        ]
        c = FindBattleShips(battle_field)
        battle_ships = c.find_battle_ships()
        self.assertEqual(1, battle_ships)

    def test_one_ship_top_left_v(self):
        battle_field = [
            ['X', '.', '.', '.', '.', '.'],
            ['X', '.', '.', '.', '.', '.'],
            ['X', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
        ]
        c = FindBattleShips(battle_field)
        battle_ships = c.find_battle_ships()
        self.assertEqual(1, battle_ships)

    def test_one_ship_middle_h(self):
        battle_field = [
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', 'X', 'X', 'X', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
        ]
        c = FindBattleShips(battle_field)
        battle_ships = c.find_battle_ships()
        self.assertEqual(1, battle_ships)

    def test_one_ship_middle_v(self):
        battle_field = [
            ['.', '.', '.', '.', '.', '.'],
            ['.', 'X', '.', '.', '.', '.'],
            ['.', 'X', '.', '.', '.', '.'],
            ['.', 'X', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
        ]
        c = FindBattleShips(battle_field)
        battle_ships = c.find_battle_ships()
        self.assertEqual(1, battle_ships)

    def test_one_ship_bottom_right_h(self):
        battle_field = [
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', 'X', 'X', 'X'],
        ]
        c = FindBattleShips(battle_field)
        battle_ships = c.find_battle_ships()
        self.assertEqual(1, battle_ships)

    def test_one_ship_bottom_right_v(self):
        battle_field = [
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', 'X'],
            ['.', '.', '.', '.', '.', 'X'],
            ['.', '.', '.', '.', '.', 'X'],
        ]
        c = FindBattleShips(battle_field)
        battle_ships = c.find_battle_ships()
        self.assertEqual(1, battle_ships)
