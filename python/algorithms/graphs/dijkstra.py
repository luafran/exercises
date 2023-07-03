import math
import unittest
import heapq
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

    def add_edge(self, source, dest, weight):
        self.adj[source][dest] = weight

        if dest not in self.adj:
            # we have to add the vertex even if it has no adjacent vertexes
            self.adj[dest] = {}

    # https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
    # See Dijkstra’s shortest path algorithm for Adjacency List using Heap in O(E logV):
    # For Dijkstra’s algorithm, it is always recommended to use Heap (or priority queue) as the required operations
    # (extract minimum and decrease key) match with the specialty of the heap (or priority queue).
    # However, the problem is, that priority_queue doesn't support the decrease key. To resolve this problem,
    # do not update a key, but insert one more copy of it. So we allow multiple instances of the same vertex in
    # the priority queue. This approach doesn't require decreasing key operations and has below important properties.
    # Whenever the distance of a vertex is reduced, we add one more instance of a vertex in priority_queue.
    # Even if there are multiple instances, we only consider the instance with minimum distance and
    # ignore other instances.
    # The time complexity remains O(E * LogV) as there will be at most O(E) vertices in the priority queue and
    # O(logE) is the same as O(logV)
    def dijkstra(self, start):
        predecessor = {
            start: None
        }
        dist = {}
        # initialize distance dict. Infinite for all nodes except start
        for v in self.adj.keys():
            dist[v] = math.inf
        dist[start] = 0

        # Create a priority queue to store vertices that are being preprocessed
        # Ordered by estimated distance
        pq = []
        print('enqueueing (', 0, start, ')')
        heapq.heappush(pq, (0, start))

        while pq:
            # The first vertex in pair is the minimum distance
            # vertex, extract it from priority queue.
            # vertex label is stored in second of pair
            distance, u = heapq.heappop(pq)
            print('### processing ({}, {}) ###'.format(distance, u))
            for v, weight in self.adj[u].items():
                print('checking', u, '-', weight, '->', v)
                print('current dist from {} to {} is {} and dist from {} to {} is {}'.format(start, u, dist[u], start, v, dist[v]))
                # If there is shorted path to v through u. Relax distance and enqueue to process that node
                if dist[v] > dist[u] + weight:
                    print('relaxing', v)
                    # update distance of v
                    dist[v] = dist[u] + weight
                    predecessor[v] = u
                    print('enqueueing (', dist[v], v, ')')
                    # Note that we are adding a possibly existing vertex in the priority queue again.
                    # This is a simplification, and it is guaranteed that we will process the lowest distance first
                    # Another alternative would be to use a Fibonacci queue
                    heapq.heappush(pq, (dist[v], v))

        for vertex, adj in self.adj.items():
            print('shortest distance from', start, 'to', vertex, ':', dist[vertex])

        print('predecessor:', predecessor)
        end = 'd'
        path = []
        while 1:
            path.append(end)
            if end == start:
                break
            end = predecessor[end]
        print('path to d', path.reverse())

    def __str__(self):
        result = []
        print('Graph:')
        for vertex, adj in self.adj.items():
            for neighbor, weight in adj.items():
                result.append('{} -- {} --> {}'.format(vertex, neighbor, weight))
        return '\n'.join(result)


class TestDijkstra(unittest.TestCase):

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
        g.dijkstra('a')
