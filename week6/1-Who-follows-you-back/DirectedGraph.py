from BFS import bfs


class NotStringNameOfNode(Exception):
    pass


class DirectedGraph:

    def __init__(self):
        self.gr_dict = {}

    def add_edge(self, node_a, node_b):
        if not (isinstance(node_a, str)) or not(isinstance(node_b, str)):
            raise NotStringNameOfNode
        if node_a not in self.gr_dict:
            self.gr_dict[node_a] = []
        self.gr_dict[node_a].append(node_b)

    def get_neighbors_for(self, node):
        if node not in self.gr_dict:
            return False
        return self.gr_dict[node]

    def path_between(self, node_a, node_b):
        if node_a not in self.gr_dict:
            self.gr_dict[node_a] = []
        if bfs(self.gr_dict, node_a, node_b) == 0:
            return False
        else:
            return True
