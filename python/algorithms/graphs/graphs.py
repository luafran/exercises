import unittest
from collections import defaultdict
from collections import deque


# Implementation that does not use queue
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-13-breadth-first-search-bfs/
def bfs1(adj, start):

    order = []
    parent = {start: None}
    level = {start: 0}

    frontier = [start]

    next_level = 1
    while frontier:
        next_frontier = []
        for u in frontier:
            print('### visiting:', u)
            order.append(u)
            for v in adj[u]:
                print('Evaluating {0} -- ({1}) --> {2}'.format(u, adj[u][v], v))
                if v not in level:
                    level[v] = next_level
                    parent[v] = u
                    next_frontier.append(v)
        frontier = next_frontier
        next_level += 1

    print('order:', order)
    print('parent:', parent)
    print('level:', level)


# Implementation using queue
def bfs2(adj, start):

    order = []
    parent = {start: None}
    level = {start: 0}

    frontier = deque()
    frontier.appendleft(start)

    while frontier:
        u = frontier.pop()
        print('### visiting:', u)
        order.append(u)
        for v in adj[u]:
            print('Evaluating {0} -- ({1}) --> {2}'.format(u, adj[u][v], v))
            if v not in level:
                level[v] = level[u] + 1
                parent[v] = u
                frontier.appendleft(v)

    print('order:', order)
    print('parent:', parent)
    print('level:', level)


def dfs_stack(adj, start):

    order = []
    parent = {}

    stack = [start]

    while stack:
        print('stack:', stack)
        u = stack.pop()
        if u not in parent:
            print('### visiting:', u)
            order.append(u)
            parent[u] = None
            for v in adj[u]:
                print('Evaluating {0} -- ({1}) --> {2}'.format(u, adj[u][v], v))
                stack.append(v)

    print('order:', order)
    print('parent:', parent)


def dfs_visit(adj, u, parent, order):

    print('### visiting:', u)
    order.append(u)
    for v in adj[u]:
        print('Evaluating {0} -- ({1}) --> {2}'.format(u, adj[u][v], v))
        if v not in parent:
            print('{0} not in parent'.format(v))
            parent[v] = u
            dfs_visit(adj, v, parent, order)
        else:
            print('{0} in parent. Cycle!'.format(v))

    print('## dfs_visit finish:', u)


def dfs_recursive(adj, start=None):

    order = []
    parent = {}

    if start is not None:
        parent[start] = None
        dfs_visit(adj, start, parent, order)
    else:
        for start in adj:
            if start not in parent:
                parent[start] = None
                dfs_visit(adj, start, parent, order)

    print('order:', order)
    topological_sort = order[::-1]
    print('topological_sort:', topological_sort)


class TestBFS(unittest.TestCase):
    # https://en.wikipedia.org/wiki/Tree_traversal
    adj_1 = defaultdict(dict)
    adj_1['F']['B'] = 1
    adj_1['F']['G'] = 1
    adj_1['B']['A'] = 1
    adj_1['B']['D'] = 1
    adj_1['D']['C'] = 1
    adj_1['D']['E'] = 1
    adj_1['G']['I'] = 1
    adj_1['I']['H'] = 1

    adj_2 = defaultdict(dict)
    adj_2['0']['1'] = 1
    adj_2['0']['2'] = 1
    adj_2['1']['2'] = 1
    adj_2['2']['0'] = 1
    adj_2['2']['3'] = 1
    adj_2['3']['3'] = 1

    def test_bfs1_adj_1_start_F(self):
        bfs1(self.adj_1, start='F')

    def test_bfs2_adj_1_start_F(self):
        bfs2(self.adj_1, start='F')

    def test_dfs_adj_1_all(self):
        dfs_recursive(self.adj_1)

    def test_dfs_adj_1_start_F(self):
        dfs_recursive(self.adj_1, start='F')

    def test_bfs1_adj_2_start_2(self):
        bfs1(self.adj_2, '2')

    def test_bfs2_adj_2_start_2(self):
        bfs2(self.adj_2, '2')

    def test_dfs_adj_2_all(self):
        dfs_recursive(self.adj_2)

    def test_dfs_stack_adj_2_start_2(self):
        dfs_stack(self.adj_2, start='2')

    def test_dfs_adj_2_start_2(self):
        dfs_recursive(self.adj_2, start='2')

    def test_dfs_adj_3_start_2(self):
        adj_3 = defaultdict(dict)
        adj_3['0']['1'] = 1
        adj_3['2']['0'] = 1
        adj_3['2']['3'] = 1
        print('dfs(adj_3, 2)')
        dfs_recursive(adj_3, start='2')
