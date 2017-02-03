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


adj_1 = defaultdict(dict)
adj_1['A']['B'] = 3
adj_1['A']['C'] = 5
adj_1['B']['C'] = 1
adj_1['B']['D'] = 4
adj_1['B']['E'] = 2
adj_1['E']['C'] = 3

print 'bfs1(adj_1, A)'
bfs1(adj_1, 'A')
print
print 'bfs2(adj_1, A)'
bfs2(adj_1, 'A')
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
