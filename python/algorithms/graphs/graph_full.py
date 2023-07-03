from collections import deque


class Vertex:
    def __init__(self, key):
        self.id = key
        self.edges = {}
        self.neighbors = {}
        self.distance = 0
        self.predecessor = None
        self.color = 'white'

    def __str__(self):
        str_edges = str(self.id) + '\n'
        str_edges += 'color: ' + self.color + '\n'
        str_edges += 'nbrs: ' + str([k.get_id() for k in self.get_connections()]) + '\n'
        for k, v in self.edges.items():
            str_edges = str_edges + '    ' + str(v) + '\n'
        return str_edges

    def __getitem__(self, key):
        for e in self.edges:
            if e.sink == key:
                return e.capacity
        return None

    def add_edge(self, edge):
        self.edges[edge.sink] = edge

    def get_edges(self):
        return self.edges.values()

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

    def __getitem__(self, v):
        # return self.get_vertex(v)
        return self.adj[v]

    def __str__(self):
        value = ''
        for k, v in self.vert_list.items():
            value += str(v) + '\n'
        return value


def bfs2(start):
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


def traverse(y):
    x = y
    while x.get_predecessor():
        print(x.get_id())
        x = x.get_predecessor()
    print(x.get_id())

def test1():
    g = Graph()

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
    print('#' * 20)
    print(g)
    print('#' * 20)
    print('number of vertex:', g.vertex_count())
    print('#' * 20)
    print('path cordoba-salta:')
    print('#' * 20)
    print(g.get_vertex('cordoba').get_edges())
    print(g.get_edges('cordoba'))
    print('#' * 20)
    bfs2(g.get_vertex('jujuy'))
    print(g)
    traverse(g.get_vertex('santa cruz'))


def test2():
    g = Graph()
    g.add_edge('A', 'B', )

if __name__ == "__main__":

    test1()
    test2()
