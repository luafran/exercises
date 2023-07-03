import math
import unittest
from collections import defaultdict


class Graph:
    def __init__(self):
        # Graph representation: A vertex can be any object that can be used as an index into a dictionary (hashable).
        # G is a dictionary, indexed by vertices. For any vertex v,
        # G[v] is itself a dictionary, indexed by the neighbors of v.
        # For any edge u->v, G[u][v] could be just the weight/capacity/cost of the edge or a more complex Edge object
        # Other common representation is G being a dictionary mapping vertices to lists of neighbors,
        # however dictionaries of edges have many advantages over lists:
        # they support fast existence tests, and they allow easy modification of the graph by edge
        # insertion and removal. Such modifications are not needed here but are important in other graph algorithms.
        # Since dictionaries obey iterator protocol, a graph represented as described here could be handed without
        # modification to an algorithm using dictionary of lists representation.
        self.adj = defaultdict(dict)

        # Useful for Bellman-Ford
        self.edges = []

    def __str__(self):
        result = []
        print('Graph:')
        for vertex, adj in self.adj.items():
            for neighbor, weight in adj.items():
                result.append('{} -- {} --> {}'.format(vertex, neighbor, weight))
        return '\n'.join(result)

    def add_edge(self, source, dest, weight):
        self.edges.append([source, dest, weight])
        self.adj[source][dest] = weight

        if dest not in self.adj:
            # we have to add the vertex even if it has no adjacent vertexes
            self.adj[dest] = {}

    def bellman_ford(self, start):
        predecessor = {
            start: None
        }
        dist = {}
        # initialize distance dict. Infinite for all nodes except start
        for v in self.adj.keys():
            dist[v] = math.inf
        dist[start] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(len(self.adj) - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, weight in self.edges:
                # print('checking', u, '-', weight, '->', v)
                # print(
                #    'current dist from {} to {} is {} and dist from {} to {} is {}'.format(start, u, dist[u], start, v,
                #                                                                            dist[v]))
                if dist[v] > dist[u] + weight:
                    # print('relaxing', v)
                    dist[v] = dist[u] + weight

        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.
        for u, v, w in self.edges:
            if dist[v] > dist[u] + w:
                print("Graph contains negative weight cycle")
                return

        for vertex, adj in self.adj.items():
            print('shortest distance from', start, 'to', vertex, ':', dist[vertex])


class TestBellmanFord(unittest.TestCase):

    def test_graph_create(self):
        # Final example
        # https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/mit6_006f11_lec16/
        g = Graph()
        g.add_edge('a', 'b', 10)
        g.add_edge('a', 'c', 3)
        g.add_edge('b', 'c', 1)
        g.add_edge('b', 'd', 2)
        g.add_edge('c', 'b', 4)
        g.add_edge('c', 'd', 8)
        g.add_edge('c', 'e', 2)
        g.add_edge('d', 'e', 7)
        g.add_edge('e', 'd', 9)
        print(g)
        g.bellman_ford('a')
