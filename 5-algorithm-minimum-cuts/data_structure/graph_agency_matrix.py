import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.edges = []
        self.vertices = []
        self.df = self.to_pandas()
        self.nx = self.to_networkx()

    def __repr__(self):
        return str(self.to_pandas())

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.vertices.append(vertex)
            self._update()

    def add_edge(self, vertex_1, vertex_2, weight: int = 1):
        if vertex_1 in self.vertices and vertex_2 in self.vertices:
            i_v1 = self.vertices.index(vertex_1)
            i_v2 = self.vertices.index(vertex_2)
            self.edges[i_v1][i_v2] = weight
            self.edges[i_v2][i_v1] = weight
            self._update()

    def to_pandas(self) -> pd.DataFrame:
        return pd.DataFrame(data=self.edges, index=self.vertices, columns=self.vertices)

    def to_networkx(self) -> nx.Graph:
        G = nx.from_numpy_matrix(
            self.df.values, parallel_edges=True, create_using=nx.MultiDiGraph()
        )
        label_mapping = {
            node_index: node_name
            for node_index, node_name in enumerate(self.df.columns)
        }
        G = nx.relabel_nodes(G, label_mapping)
        return G

    def _update(self):
        self.df = self.to_pandas()
        self.nx = self.to_networkx()

    def draw(self):
        plt.figure()
        nx.draw(self.nx, with_labels=True)
        plt.show()


if __name__ == "__main__":
    g = Graph()
    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")
    g.add_edge("a", 12)
    g.add_edge("a", "c")
    G = g.nx
    print(nx.spring_layout(G))
    g.draw()
