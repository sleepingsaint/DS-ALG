# creating the node object class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

# creating the edge object Class
class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

# creating the graph object class
class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges
        self.node_map = {}
        self.node_names = []

    def insert_node(self, value):
        node = Node(value)
        self.nodes.append(node)
        self.node_map[value] = node
        return node

    def set_node_names(self, names):
        self.node_names = list(names)

    def insert_edge(self, value, node_from, node_to):
        nodes = {
            node_from: None,
            node_to: None
        }
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
        for node in nodes:
            nodes[node] = nodes[node] or self.insert_node(node)
        edge = Edge(value, nodes[node_from], nodes[node_to])
        self.edges.append(edge)
        nodes[node_from].edges.append(edge)
        nodes[node_to].edges.append(edge)

    def get_edge_list(self):
        return [(edge.value, edge.node_from.value, edge.node_to.value) for edge in self.edges]

    def get_edge_list_names(self):
        # (Edge Value, From Node Name, To Node Name)
        return [(edge.value, self.node_names[edge.node_from.value], self.node_names[edge.node_to.value])
                for edge in self.edges]

    def get_adjacency_list(self):
        max_index = self.max_index()
        adjacency_list = [[] for _ in range(max_index)]
        for edge in self.edges:
            adjacency_list[edge.node_from.value].append((edge.node_from.value, edge.node_to.value, edge.value))
        return [a or None for a in adjacency_list]

    def get_adjacency_list_names(self):
        adjacency_list = self.get_adjacency_list()

        def convert_name(pair):
            node_from, node_to, value = pair
            return (self.node_names[node_from], self.node_names[node_to], value)

        def map_conversion(adjacency_list_for_node):
            if adjacency_list_for_node is None:
                return None
            return map(convert_name, adjacency_list_for_node)

        return [list(map_conversion(ad_list))
                for ad_list in adjacency_list]

    def get_adjacency_matrix(self):
        max_index = self.max_index()
        adjacency_matrix = [[0]*max_index for _ in range(max_index)]
        for edge in self.edges:
            adjacency_matrix[edge.node_from.value][edge.node_to.value] = edge.value
        return adjacency_matrix

    def dfs(self, value):
        self.clear_visited()
        start_node = self.find_node(value)
        return self.dfs_helper(start_node)

    def dfs_helper(self, start_node):
        ret_list = [start_node.value]
        start_node.visited = True
        edges_out = [e for e in start_node.edges
                     if e.node_to.value != start_node.value]
        for e in edges_out:
            if e.node_to.visited is False:
                ret_list.extend(self.dfs_helper(e.node_to))
        return ret_list

    def bfs(self, value):
        self.clear_visited()
        start_node = self.find_node(value)
        ret_list = []
        queue = [start_node]
        start_node.visited = True
        while queue:
            node = queue.pop(0)
            ret_list.append(node.value)
            if node.edges:
                for e in node.edges:
                    if e.node_to.visited is False:
                        queue.append(e.node_to)
                        e.node_to.visited = True
        return ret_list

    def dfs_name(self, value):
        dfs_name_list = self.dfs(value)
        ret_list = []
        for val in dfs_name_list:
            ret_list.append(self.node_names[val])
        return ret_list

    def bfs_name(self, value):
        bfs_name_list = self.bfs(value)
        ret_list = []
        for val in bfs_name_list:
            ret_list.append(self.node_names[val])
        return ret_list

    def max_index(self):
        max_index = 0
        for node in self.nodes:
            if max_index < node.value:
                max_index = node.value
        return max_index + 1

    def find_node(self, value):
        return self.node_map.get(value)

    def clear_visited(self):
        for node in self.nodes:
            node.visited = False

# test cases
graph = Graph()

graph.set_node_names(('Mountain View',   # 0
                      'San Francisco',   # 1
                      'London',          # 2
                      'Shanghai',        # 3
                      'Berlin',          # 4
                      'Sao Paolo',       # 5
                      'Bangalore'))      # 6
# adding / inserting the edges
graph.insert_edge(51, 0, 1)     # MV <-> SF
graph.insert_edge(51, 1, 0)     # SF <-> MV
graph.insert_edge(9950, 0, 3)   # MV <-> Shanghai
graph.insert_edge(9950, 3, 0)   # Shanghai <-> MV
graph.insert_edge(10375, 0, 5)  # MV <-> Sao Paolo
graph.insert_edge(10375, 5, 0)  # Sao Paolo <-> MV
graph.insert_edge(9900, 1, 3)   # SF <-> Shanghai
graph.insert_edge(9900, 3, 1)   # Shanghai <-> SF
graph.insert_edge(9130, 1, 4)   # SF <-> Berlin
graph.insert_edge(9130, 4, 1)   # Berlin <-> SF
graph.insert_edge(9217, 2, 3)   # London <-> Shanghai
graph.insert_edge(9217, 3, 2)   # Shanghai <-> London
graph.insert_edge(932, 2, 4)    # London <-> Berlin
graph.insert_edge(932, 4, 2)    # Berlin <-> London
graph.insert_edge(9471, 2, 5)   # London <-> Sao Paolo
graph.insert_edge(9471, 5, 2)   # Sao Paolo <-> London

print(graph.bfs_name(1))
print(graph.dfs_name(1))