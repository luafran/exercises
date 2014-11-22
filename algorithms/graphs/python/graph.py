class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.sink = v
        self.capacity = w

    def __repr__(self):
        return "%s->%s:%s" % (self.source, self.sink, self.capacity)


class Graph(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}

    def add_vertex(self, vertex):
        self.adj[vertex] = []

    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u, v, w)
        redge = Edge(v, u, w)
        edge.redge = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0

    def get_edges(self, v):
        return self.adj[v]

    def vertex_count(self):
        return len(self.adj)

    def find_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and not (edge, residual) in path:
                result = self.find_path(edge.sink, sink, path + [(edge, residual)])
                if result is not None:
                    return result

    def __repr__(self):
        return repr(self.adj)

    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        while path is not None:
            flow = min(res for edge, res in path)
            for edge, res in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.get_edges(source))

# Dijkstra's algorithm for shortest paths
# David Eppstein, UC Irvine, 4 April 2002

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
    estimated_distances = priorityDictionary()   # est.dist. of non-final vert.
    estimated_distances[start] = 0

    for vertex in estimated_distances:
        final_distances[vertex] = estimated_distances[vertex]
        if vertex == end:
            break

        for edge in graph[vertex]:
            path_distance = final_distances[vertex] + graph[vertex][edge]
            if edge in final_distances:
                if path_distance < final_distances[edge]:
                    raise ValueError("Dijkstra: found better path to already-final vertex")
            elif edge not in estimated_distances or path_distance < estimated_distances[edge]:
                estimated_distances[edge] = path_distance
                predecessors[edge] = vertex

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
    path = []
    while 1:
        path.append(end)
        if end == start:
            break
        end = predecessors[end]
    path.reverse()
    return path

if __name__ == "__main__":
    g = Graph()
    map(g.add_vertex, ['jujuy', 'salta', 'tucuman', 'formosa', 'chaco',
                       'catamarca', 'santiago del estero',
                       'misiones', 'corrientes', 'entre rios',
                       'la rioja', 'san juan', 'mendoza',
                       'cordoba', 'san luis', 'santa fe', 'buenos aires', 'la pampa',
                       'neuquen', 'rio negro', 'chubut', 'santa cruz', 'tierra del fuego'])
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
    g.add_edge('catamarca', 'cordoba', 1)
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
    print g
    print 'number of vertex:', g.vertex_count()
    print 'path cordoba-santa cruz:', shortest_path(g, 'cordoba', 'santa cruz')

    #print g.max_flow('s','t')