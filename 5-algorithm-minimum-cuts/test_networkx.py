import networkx as nx
from utils.other import name_str
import matplotlib.pyplot as plt


def test_add_nodes(G):
    # Add single node
    G.add_node(1)
    # Add multiple nodes
    G.add_nodes_from([2, 3])


def test_add_edges(G):
    # Add single node
    G.add_edge(1, 2)
    try:
        G.add_edge(4, 5)
    # Doesn't run the except clause. It creates the nonexistent nodes for the edge
    except:
        print("These nodes don't exist")
    # Add multiple edges
    G.add_edges_from([[1, 2], [1, 3]])


def print_number_nodes_edges(G, local_variables):
    print(f"{name_str(G, local_variables)} has {G.number_of_nodes()} nodes")
    print(f"{name_str(G, local_variables)} has {G.number_of_edges()} edges")


def print_nodes_edges(G, local_variables):
    print(f"{name_str(G, local_variables)} nodes: {G.nodes()}")
    print(f"{name_str(G, local_variables)} edges: {G.edges()}")


def test_remove_edge(G):
    print("Remove edge between 1 and 3")
    G.remove_edge(1, 3)


if __name__ == "__main__":
    # Initialize
    G_test = nx.Graph()
    test_add_nodes(G_test)
    test_add_edges(G_test)
    print_number_nodes_edges(G_test, locals())
    print_nodes_edges(G_test, locals())
    print(f"Number of edges to 1: {G_test.degree[1]}")
    test_remove_edge(G_test)
    print_nodes_edges(G_test, locals())
    # Remove all nodes and edges
    # print('Clear G_test')
    # G_test.clear()
    # print_number_nodes_edges(G_test, locals())
    fig = plt.figure()
    nx.draw_shell(G_test, with_labels=True, font_weight="bold")
    plt.show()
