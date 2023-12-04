from typing import Tuple, Set, List


class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = set()
        print(self.__repr__())

    def __repr__(self):
        return f"Vertex({self.name})"


class Edge:
    def __init__(self, vertex_1: Vertex, vertex_2: Vertex):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        print(self.__repr__())

    def __repr__(self):
        return f"{self.vertex_1.__repr__()} <---> {self.vertex_2.__repr__()}"


class Graph:
    def __init__(self, vertices: Set[Vertex] = None, edges: List[Edge] = None):
        if vertices is None:
            vertices = set()
        if edges is None:
            edges = []
        self.vertices = vertices
        self.edges = edges

    def add_vertex(self, v: Vertex):
        self.vertices.add(v)

    def add_edge(self, e: Edge):
        if e.vertex_1 not in self.vertices or e.vertex_2 not in self.vertices:
            raise ReferenceError(
                "The vertices of the edge that you try to add the graph don't belong to it"
            )
        self.edges.append(e)

    def __repr__(self):
        repr_vertices = self.vertices.__repr__()
        repr_edges = self.edges.__repr__()
        return f"Vertices: {repr_vertices}\n Edges: {repr_edges}"


if __name__ == "__main__":
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    e = Edge(v1, v2)
    e2 = Edge(v1, v3)
    g = Graph()
    g.add_vertex(v1)
    g.add_vertex(v2)
    g.add_vertex(v3)
    g.add_edge(e)
    g.add_edge(e2)
    print(g)
