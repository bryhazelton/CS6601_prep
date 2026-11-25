
class Graph:
    
    def __init__(self):
        self.adjaceny = {}
        
    def add_node(self, node):
        self.adjaceny[node] = {}
    
    def add_edge(self, u, v, weight):
        pass
    
    def neighbors(self, node):
        pass
    
    def get_edge_weight(self, u, v):
        pass
    
    def path_cost(self, path):
        pass
    
    
    
    
    
    
if __name__== "__main__":
    
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    
    print(g.adjaceny)