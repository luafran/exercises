import unittest
from collections import defaultdict


def dfs(adj, start):
    level_number = 0
    levels = {
        start: level_number,
    }
    order = []
    predecessors = {
        start: None,
    }
    vertexes_in_level = [start]
    while vertexes_in_level:
        print('processing level', level_number)
        vertexes_in_next_level = []
        for vertex in vertexes_in_level:
            print('visiting', vertex)
            order.append(vertex)
            for v in adj[vertex]:
                print('v:', v)
                if v not in levels:
                    levels[v] = level_number + 1
                    predecessors[v] = vertex
                    vertexes_in_next_level.append(v)
        level_number += 1
        vertexes_in_level = vertexes_in_next_level

    print('levels', levels)
    print('order', order)
    print('predecessors', predecessors)


class TestsBFS(unittest.TestCase):

    def test_graph_01(self):
        adj = defaultdict(dict)
        adj['A']['B'] = 1
        adj['B']['C'] = 1
        adj['C']['D'] = 1
        adj['C']['E'] = 1
        adj['D']['F'] = 1
        adj['E']['F'] = 1
        dfs(adj, 'A')

    def test_graph_02(self):
        adj = defaultdict(dict)
        adj['A']['B'] = 1
        adj['A']['E'] = 1
        adj['B']['C'] = 1
        adj['B']['D'] = 1
        adj['D']['E'] = 1
        adj['E']['F'] = 1
        adj['E']['G'] = 1
        adj['E']['H'] = 1
        adj['H']['1'] = 1
        dfs(adj, 'A')
