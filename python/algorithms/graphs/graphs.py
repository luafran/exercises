from collections import defaultdict
from collections import deque

g_parent = []


# Implementation using queue
def bfs1(adj, start):

    # If we need to do something on start node, it should be done here
    level = {start: 0}
    parent = {start: None}
    frontier = deque()

    frontier.appendleft(start)

    while frontier:
        u = frontier.pop()
        for v in adj[u]:
            if v not in level:
                print '{0} -- {1} --> {2}'.format(u, adj[u][v], v)
                print 'visiting:', v
                level[v] = level[u] + 1
                parent[v] = u
                frontier.appendleft(v)

    print 'level:', level
    print 'parent:', parent


# Implementation that does not use queue
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-13-breadth-first-search-bfs/
def bfs2(adj, start):

    # If we need to do something on start node, it should be done here
    level = {start: 0}
    parent = {start: None}
    i = 1
    frontier = [start]

    while frontier:
        next_frontier = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    print '{0} -- {1} --> {2}'.format(u, adj[u][v], v)
                    print 'visiting:', v
                    level[v] = i
                    parent[v] = u
                    next_frontier.append(v)
        frontier = next_frontier
        i += 1

    print 'level:', level
    print 'parent:', parent


def dfs_visit(adj, start, parent, order):
    print 'dfs_visit start:', start
    for v in adj[start]:
        if v not in parent:
            print '{0} -- {1} --> {2}'.format(start, adj[start][v], v)
            print 'visiting:', v
            parent[v] = start
            dfs_visit(adj, v, parent, order)

    order.append(start)
    print 'dfs_visit finish:', start


def dfs(adj):
    parent = {}
    order = []
    for start in adj:
        if start not in parent:
            parent[start] = None
            dfs_visit(adj, start, parent, order)
    topological_sort = order[::-1]
    print 'topological_sort:', topological_sort


def dfs_stack(adj):
    parent = {}
    stack = []
    for start in adj:
        stack.append(start)
        while stack:
            v = stack.pop()
            if v not in parent:
                parent[v]


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

print 'bfs1(adj_1, F)'
bfs1(adj_1, 'F')
print
print 'bfs2(adj_1, F)'
bfs2(adj_1, 'F')
print

print 'dfs(adj_1)'
dfs(adj_1)
print

adj_2 = defaultdict(dict)
adj_2['A']['B'] = 1
adj_2['A']['C'] = 1
adj_2['B']['D'] = 1
adj_2['C']['E'] = 1
adj_2['D']['F'] = 1
adj_2['E']['G'] = 1

print 'bfs1(adj_2, A)'
bfs1(adj_2, 'A')
print
print 'bfs2(adj_2, A)'
bfs2(adj_2, 'A')
print

print 'dfs(adj_2)'
dfs(adj_2)
