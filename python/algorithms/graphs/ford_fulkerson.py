import unittest
from collections import defaultdict


class Edge(object):
    def __init__(self, source, dest, capacity, flow=0):
        self.source = source
        self.dest = dest
        self.capacity = capacity
        self.flow = flow
        self.r_edge = None

    def __str__(self):
        return '{}->{}": "{}/{}'.format(self.source, self.dest, self.flow, self.capacity)

    def __repr__(self):
        return '{}->{}": "{}/{}'.format(self.source, self.dest, self.flow, self.capacity)


class FlowNetwork(object):
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

    def add_edge(self, source, dest, capacity=0):
        if source == dest:
            raise ValueError("source == sink")

        edge = Edge(source, dest, capacity)
        r_edge = Edge(dest, source, 0)
        edge.r_edge = r_edge
        r_edge.r_edge = edge
        self.adj[source][dest] = edge
        self.adj[dest][source] = r_edge

    def __str__(self):
        result = []
        print('Graph:')
        for vertex, neighbors in self.adj.items():
            # [print(edge) for edge in neighbors.values() if edge.capacity > 0]
            [print(edge) for edge in neighbors.values()]
        return '\n'.join(result)

    def find_augmenting_path(self, source, sink, path):
        # print('find_augmenting_path({}, {}, {})'.format(source, sink, path))
        if source == sink:
            return path
        for edge in self.adj[source].values():
            # reverse edges may have a negative flow (always equal to forward edge current flow) and
            # always 0 capacity, so residual could be positive for them.
            residual = edge.capacity - edge.flow
            # print('edge', edge, 'residual:', residual)
            if residual > 0 and not (edge, residual) in path:
                # print('adding', (edge, residual), 'to path')
                result = self.find_augmenting_path(edge.dest, sink, path + [(edge, residual)])
                # if this is a result from a call that got a path return that
                if result:
                    return result
        return None

    def max_flow(self, source, sink):
        path = self.find_augmenting_path(source, sink, [])
        while path:
            flow = min(residual for edge, residual in path)
            print('#### path:', path, 'can take flow:', flow)
            for edge, residual in path:
                edge.flow += flow
                # If in the path found using residual network edge is a reverse edge,
                # then edge.redge is the original edge and here we are "cancelling" that flow
                edge.r_edge.flow -= flow
            print(self)
            path = self.find_augmenting_path(source, sink, [])
        out_flow_at_s = sum(edge.flow for edge in self.adj[source].values())
        in_flow_at_t = sum(edge.flow for edge in self.adj[sink].values())
        print('out flow at s:', out_flow_at_s)
        print('in flow at t:', in_flow_at_t)
        return out_flow_at_s


class TestFlowNetwork(unittest.TestCase):

    def test_01(self):
        # https://www.topcoder.com/thrive/articles/Maximum%20Flow:%20Part%20One
        g = FlowNetwork()
        g.add_edge('s', 'a', 3)
        g.add_edge('s', 'b', 1)
        g.add_edge('a', 'c', 3)
        g.add_edge('b', 'c', 5)
        g.add_edge('b', 'd', 4)
        g.add_edge('c', 't', 2)
        g.add_edge('d', 'e', 2)
        g.add_edge('e', 't', 3)
        print(g)
        g.max_flow('s', 't')

    def test_02(self):
        g = FlowNetwork()
        g.add_edge('s', 'o', 3)
        g.add_edge('s', 'p', 3)
        g.add_edge('o', 'p', 2)
        g.add_edge('o', 'q', 3)
        g.add_edge('p', 'r', 2)
        g.add_edge('r', 't', 3)
        g.add_edge('q', 'r', 4)
        g.add_edge('q', 't', 2)
        gp = repr(g)
        gp = gp.replace("'", '"')
        print(gp)
        print(g.max_flow('s', 't'))
