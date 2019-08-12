# creating Node object class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

# creating edge object class
class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

# creating graph object class
class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    # class functions
    def insert_node(self, value):
        node = Node(value)
        self.nodes.append(node)

    def insert_edge(self, value, node_from, node_to):
        nodes = {
            node_from: None,
            node_to: None
        }
        for node in self.nodes:
            if node.value in nodes:
                nodes[value] = node
        if nodes[node_from] is None:
            nodes[node_from] = Node(node_from)
            self.nodes.append(nodes[node_from])
        if nodes[node_to] is None:
            nodes[node_to] = Node(node_to)
            self.nodes.append(nodes[node_to])
        edge = Edge(value, nodes[node_from], nodes[node_to])
        self.edges.append(edge)
        nodes[node_from].edges.append(edge)
        nodes[node_to].edges.append(edge)

    # for getting the edge list of the graph
    # in the format (edge.value, from node value, to node value)
    def get_edge_list(self):
        edge_list = []
        if self.edges:
            for edge in self.edges:
                ed = (edge.value, edge.node_from.value, edge.node_to.value)
                edge_list.append(ed)
        return edge_list

    # getting the adjacency list
    # [(node to value, edge value)]
    def get_adjacency_list(self):
        max_index = self.get_max_index()
        adjacency_list = [None for _ in range(max_index + 1)]
        for edge in self.edges:
            if adjacency_list[edge.node_from.value] is None:
                adjacency_list[edge.node_from.value] = [(edge.node_to.value, edge.value)]
            else:
                adjacency_list[edge.node_from.value].append((edge.node_to.value, edge.value))
        # for node in self.nodes:
        #     for edge in node.edges:
        #         adjacent_edge = (edge.node_to.value, edge.value)
        #         if adjacency_list[edge.node_from.value] is None:
        #             adjacency_list[edge.node_from.value] = [adjacent_edge]
        #         else:
        #             if adjacent_edge not in adjacency_list[edge.node_from.value]:
        #                 adjacency_list[edge.node_from.value].append(adjacent_edge)
        return adjacency_list

    # getting the adjacency matrix
    def get_adjacency_matrix(self):
        max_index = self.get_max_index()
        adjacency_matrix = [[0]*(max_index + 1) for _ in range(max_index + 1)]
        for edge in self.edges:
            adjacency_matrix[edge.node_from.value][edge.node_to.value] = edge.value
        # for node in self.nodes:
        #     for edge in node.edges:
        #         adjacency_matrix[edge.node_from.value][edge.node_to.value] = edge.value
        return adjacency_matrix

    # helper class function
    def get_max_index(self):
        max_index = 0
        for node in self.nodes:
            if node.value > max_index:
                max_index = node.value
        return max_index


# test cases
graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)

# [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print(graph.get_edge_list())
# [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print(graph.get_adjacency_list())
# [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print(graph.get_adjacency_matrix())













































