from collections import deque


class Vertex:
    def __init__(self, key):
        self.id = key
        self.edges = []
        self.neighbors = {}
        self.distance = 0
        self.predecessor = None
        self.color = 'white'

    #def __str__(self):
    #    return str(self.id) + ' connectedTo: ' + str([x.id for x in self.get_connections()])

    def __str__(self):
        str_edges = str(self.id) + '\n'
        str_edges += 'color: ' + self.color + '\n'
        str_edges += 'nbrs: ' + str([k.get_id() for k in self.get_connections()]) + '\n'
        for e in self.get_edges():
            str_edges = str_edges + '    ' + str(e) + '\n'
        return str_edges
        #return str(self.id) + '\n' + str([x for x in self.get_edges()])

    #def __repr__(self):
    #    return str([x for x in self.get_edges()]) + '\n'

    def __getitem__(self, key):
        for e in self.edges:
            if e.sink == key:
                return e.capacity
        return None

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_edges(self):
        return self.edges

    def add_neighbor(self, nbr, weight=0):
        self.neighbors[nbr] = weight

    def get_neighbors(self):
        return self.neighbors

    def get_connections(self):
        return self.neighbors.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.neighbors.get(nbr)

    def get_distance(self):
        return self.distance

    def set_distance(self, d):
        self.distance = d

    def get_predecessor(self):
        return self.predecessor

    def set_predecessor(self, p):
        self.predecessor = p

    def get_color(self):
        return self.color

    def set_color(self, c):
        self.color = c


class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.sink = v
        self.capacity = w
        self.redge = None

    def __repr__(self):
        return '"%s" -> "%s": %s' % (self.source, self.sink, self.capacity)


class Graph(object):
    def __init__(self):
        self.adj = {}
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):

        self.adj[key] = {}

        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        return self.vert_list.get(key)

    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")

        if u not in self.vert_list:
            self.add_vertex(u)

        if v not in self.vert_list:
            self.add_vertex(v)

        self.vert_list[u].add_neighbor(self.vert_list[v], w)
        self.vert_list[v].add_neighbor(self.vert_list[u], w)

        # Compact representation
        self.adj[u][v] = w
        self.adj[v][u] = w

        edge = Edge(u, v, w)
        redge = Edge(v, u, w)
        self.vert_list[u].add_edge(edge)
        self.vert_list[v].add_edge(redge)
        edge.redge = redge
        redge.redge = edge

    def get_edges(self, v):
        return self.get_vertex(v).get_edges()

    def vertex_count(self):
        return len(self.vert_list)

    def find_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and not (edge, residual) in path:
                result = self.find_path(edge.sink, sink, path + [(edge, residual)])
                if result is not None:
                    return result

    def __getitem__(self, v):
        #return self.get_vertex(v)
        return self.adj[v]

    def __repr__(self):
        value = ''
        for k, v in self.vert_list.items():
            value += str(v) + '\n'
        return value

    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        while path is not None:
            flow = min(res for edge, res in path)
            for edge, res in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.get_edges(source))


def bfs(start):
    start.set_distance(0)
    start.set_predecessor(None)
    q = deque()
    q.appendleft(start)
    while len(q) > 0:
        current_vert = q.pop()
        for nbr in current_vert.get_connections():
            if nbr.get_color() == 'white':
                nbr.set_color('gray')
                nbr.set_distance(current_vert.get_distance() + 1)
                nbr.set_predecessor(current_vert)
                q.appendleft(nbr)
        current_vert.set_color('black')

def bfs2(start):
    start.set_distance(0)
    start.set_predecessor(None)
    q = deque()
    q.appendleft(start)
    while len(q) > 0:
        current_vert = q.pop()
        for edge in current_vert.get_edges():
            if nbr.get_color() == 'white':
                nbr.set_color('gray')
                nbr.set_distance(current_vert.get_distance() + 1)
                nbr.set_predecessor(current_vert)
                q.appendleft(nbr)
        current_vert.set_color('black')


def traverse(y):
    x = y
    while x.get_predecessor():
        print(x.get_id())
        x = x.get_predecessor()
    print(x.get_id())


# Dijkstra's algorithm for shortest paths
# David Eppstein, UC Irvine, 4 April 2002

# G = {'s':{'u':10, 'x':5}, 'u':{'v':1, 'x':2}, 'v':{'y':4}, 'x':{'u':3, 'v':9, 'y':2}, 'y':{'s':7, 'v':6}}
# The shortest path from s to v is ['s', 'x', 'u', 'v'] and has length 9.

# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228
from priodict import priorityDictionary


def dijkstra(graph, start, end=None):
    """
    Find shortest paths from the start vertex to all
    vertices nearer than or equal to the end.

    The input graph G is assumed to have the following
    representation: A vertex can be any object that can
    be used as an index into a dictionary.  G is a
    dictionary, indexed by vertices.  For any vertex v,
    G[v] is itself a dictionary, indexed by the neighbors
    of v.  For any edge v->w, G[v][w] is the length of
    the edge.  This is related to the representation in
    <http://www.python.org/doc/essays/graphs.html>
    where Guido van Rossum suggests representing graphs
    as dictionaries mapping vertices to lists of neighbors,
    however dictionaries of edges have many advantages
    over lists: they can store extra information (here,
    the lengths), they support fast existence tests,
    and they allow easy modification of the graph by edge
    insertion and removal.  Such modifications are not
    needed here but are important in other graph algorithms.
    Since dictionaries obey iterator protocol, a graph
    represented as described here could be handed without
    modification to an algorithm using Guido's representation.

    Of course, G and G[v] need not be Python dict objects;
    they can be any other object that obeys dict protocol,
    for instance a wrapper in which vertices are URLs
    and a call to G[v] loads the web page and finds its links.

    The output is a pair (D,P) where D[v] is the distance
    from start to v and P[v] is the predecessor of v along
    the shortest path from s to v.

    Dijkstra's algorithm is only guaranteed to work correctly
    when all edge lengths are positive. This code does not
    verify this property for all edges (only the edges seen
    before the end vertex is reached), but will correctly
    compute shortest paths even for some graphs with negative
    edges, and will raise an exception if it discovers that
    a negative edge has caused it to make a mistake.
    """

    final_distances = {}  # dictionary of final distances
    predecessors = {}  # dictionary of predecessors
    estimated_distance = priorityDictionary()   # est.dist. of non-final vert.
    estimated_distance[start] = 0

    # print 'estimated_distance = ', estimated_distance
    for v in estimated_distance:
        final_distances[v] = estimated_distance[v]
        if v == end:
            break

        for w in graph[v]:
            # print 'v:', v, 'w:', w
            vw_length = final_distances[v] + graph[v][w]
            # print 'vw_length=', vw_length
            if w in final_distances:
                if vw_length < final_distances[w]:
                    raise ValueError("Dijkstra: found better path to already-final vertex")
            elif w not in estimated_distance or vw_length < estimated_distance[w]:
                # print 'adding estimated_distance for ', w
                estimated_distance[w] = vw_length
                predecessors[w] = v

    return final_distances, predecessors


def shortest_path(graph, start, end):
    """
    Find a single shortest path from the given start vertex
    to the given end vertex.
    The input has the same conventions as Dijkstra().
    The output is a list of the vertices in order along
    the shortest path.
    """

    final_distances, predecessors = dijkstra(graph, start, end)
    cost = final_distances[end]
    path = []
    while 1:
        path.append(end)
        if end == start:
            break
        end = predecessors[end]

    path.reverse()
    return path, cost


def test1():
    g = Graph()
    #map(g.add_vertex, ['jujuy', 'salta', 'tucuman', 'formosa', 'chaco',
    #                   'catamarca', 'santiago del estero',
    #                   'misiones', 'corrientes', 'entre rios',
    #                   'la rioja', 'san juan', 'mendoza',
    #                   'cordoba', 'san luis', 'santa fe', 'buenos aires', 'la pampa',
    #                   'neuquen', 'rio negro', 'chubut', 'santa cruz', 'tierra del fuego'])

    g.add_edge('jujuy', 'salta', 1)
    g.add_edge('salta', 'formosa', 1)
    g.add_edge('salta', 'chaco', 1)
    g.add_edge('salta', 'santiago del estero', 1)
    g.add_edge('salta', 'tucuman', 1)
    g.add_edge('salta', 'catamarca', 1)
    g.add_edge('tucuman', 'santiago del estero', 1)
    g.add_edge('tucuman', 'catamarca', 1)
    g.add_edge('formosa', 'chaco', 1)
    g.add_edge('chaco', 'corrientes', 1)
    g.add_edge('chaco', 'santa fe', 1)
    g.add_edge('chaco', 'santiago del estero', 1)
    g.add_edge('catamarca', 'santiago del estero', 1)
    g.add_edge('catamarca', 'cordoba', 2)
    g.add_edge('catamarca', 'la rioja', 1)
    g.add_edge('santiago del estero', 'santa fe', 1)
    g.add_edge('santiago del estero', 'cordoba', 1)
    g.add_edge('misiones', 'corrientes', 1)
    g.add_edge('corrientes', 'entre rios', 1)
    g.add_edge('corrientes', 'santa fe', 1)
    g.add_edge('entre rios', 'buenos aires', 1)
    g.add_edge('entre rios', 'santa fe', 1)
    g.add_edge('la rioja', 'cordoba', 1)
    g.add_edge('la rioja', 'san luis', 1)
    g.add_edge('la rioja', 'san juan', 1)
    g.add_edge('san juan', 'san luis', 1)
    g.add_edge('san juan', 'mendoza', 1)
    g.add_edge('mendoza', 'san luis', 1)
    g.add_edge('mendoza', 'la pampa', 1)
    g.add_edge('mendoza', 'neuquen', 1)
    g.add_edge('mendoza', 'rio negro', 1)
    g.add_edge('cordoba', 'santa fe', 1)
    g.add_edge('cordoba', 'buenos aires', 1)
    g.add_edge('cordoba', 'la pampa', 1)
    g.add_edge('cordoba', 'san luis', 1)
    g.add_edge('san luis', 'la pampa', 1)
    g.add_edge('santa fe', 'buenos aires', 1)
    g.add_edge('buenos aires', 'rio negro', 1)
    g.add_edge('buenos aires', 'la pampa', 1)
    g.add_edge('la pampa', 'rio negro', 1)
    g.add_edge('la pampa', 'neuquen', 1)
    g.add_edge('neuquen', 'rio negro', 1)
    g.add_edge('rio negro', 'chubut', 1)
    g.add_edge('chubut', 'santa cruz', 1)
    g.add_edge('santa cruz', 'tierra del fuego', 1)
    print '#' * 20
    print g
    print '#' * 20
    print 'number of vertex:', g.vertex_count()

    #print 'path cordoba-salta:'
    #path, cost = shortest_path(g, 'cordoba', 'salta')
    #print path
    #print 'cost =', cost

    #print g.get_vertex('cordoba').get_edges()
    #print g.get_edges('cordoba')

    bfs(g.get_vertex('jujuy'))
    print g
    traverse(g.get_vertex('santa cruz'))


def test2():
    g = Graph()
    g.add_edge('jujuy', 'salta', 1)
    g.add_edge('salta', 'formosa', 1)
    g.add_edge('salta', 'chaco', 1)
    g.add_edge('salta', 'santiago del estero', 1)
    g.add_edge('salta', 'tucuman', 1)
    g.add_edge('salta', 'catamarca', 1)
    g.add_edge('tucuman', 'santiago del estero', 1)
    g.add_edge('tucuman', 'catamarca', 1)

    gp = repr(g)
    gp = gp.replace("'", '"')
    print gp

    bfs(g.get_vertex('jujuy'))
    traverse(g.get_vertex('tucuman'))

if __name__ == "__main__":

    test1()
    #print g.max_flow('s','t')