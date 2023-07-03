import unittest


class Edge(object):
    def __init__(self, u, v, capacity, flow=0):
        self.source = u
        self.sink = v
        self.capacity = capacity
        self.flow = flow

    def set_flow(self, flow):
        self.flow = flow

    def __str__(self):
        return '{}->{}": "{}/{}'.format(self.source, self.sink, self.flow, self.capacity)

    def __repr__(self):
        return '{}->{}": "{}/{}'.format(self.source, self.sink, self.flow, self.capacity)


class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}

    def add_edge(self, u, v, capacity=0):
        if u == v:
            raise ValueError("u == v")
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        edge = Edge(u, v, capacity)
        redge = Edge(v, u, 0)
        edge.redge = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0

    def __str__(self):
        result = []
        print('Graph:')
        for vertex, neighbors in self.adj.items():
            [print(edge) for edge in neighbors if edge.capacity > 0]
        return '\n'.join(result)

    def find_augmenting_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.adj[source]:
            residual = edge.capacity - self.flow[edge]
            # print('edge', edge, '{}/{}'.format(self.flow[edge], edge.capacity), 'residual:', residual)
            if residual > 0 and not (edge, residual) in path:
                # print('adding', (edge, residual), 'to path')
                result = self.find_augmenting_path(edge.sink, sink, path + [(edge, residual)])
                if result is not None:
                    return result

    def max_flow(self, source, sink):
        path = self.find_augmenting_path(source, sink, [])
        while path is not None:
            flow = min(residual for edge, residual in path)
            print('path:', path, 'flow:', flow)
            for edge, residual in path:
                edge.flow += flow
                edge.redge.flow -= flow
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            print(self)
            path = self.find_augmenting_path(source, sink, [])
        out_flow_at_s = sum(self.flow[edge] for edge in self.adj[source])
        in_flow_at_t = sum(self.flow[edge] for edge in self.adj[sink])
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
        print(g.max_flow('s', 't'))

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
