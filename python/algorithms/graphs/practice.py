import unittest
from collections import defaultdict


class Edge:
    def __init__(self, source, sink, capacity, flow=0):
        self.source = source
        self.sink = sink
        self.capacity = capacity
        self.flow = flow
        self.redge = None


class FlowNetwork:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, source, sink, capacity):
        if source == sink:
            raise ValueError('source == sink')
        edge = Edge(source, sink, capacity)
        redge = Edge(sink, source, 0)
        edge.redge = redge
        redge.redge = edge
        self.adj[source].append(edge)
        self.adj[sink].append(redge)

    def find_augmenting_path(self, source, sink, path):
        if source == sink:
            return path

        for edge in self.adj[source]:
            # reverse edges may have negative flow and always 0 capacity, so residual could be positive
            residual = edge.capacity - edge.flow
            if residual > 0 and (edge, residual) not in path:
                result = self.find_augmenting_path(edge.dest, sink, path + [(edge, residual)])
                if result:
                    return result

    def max_flow(self, source, sink):
        path = self.find_augmenting_path(source, sink, [])
        while path:
            flow = min(residual for edge, residual in path)
            for edge, residual in path:
                edge.flow += flow
                # If in the path found using residual network edge is a reverse edge,
                # then edge.redge is the original edge and here we are "cancelling" that flow
                edge.r_edge.flow -= flow


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
