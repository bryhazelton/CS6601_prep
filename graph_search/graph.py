
class Graph:
    
    def __init__(self):
        self.adjacency = {}
        
    def add_node(self, node):
        self.adjacency.setdefault(node, {})
    
    def add_edge(self, u, v, weight):
        self.add_node(u)
        self.add_node(v)
        self.adjacency[u][v] = weight
        self.adjacency[v][u] = weight
    
    def neighbors(self, node):
        
        return self.adjacency[node].keys()
        
    def get_edge_weight(self, u, v):
        
        return self.adjacency[u][v]
    
    def path_cost(self, path):
        pass
    
    
    
    
    
    
if __name__== "__main__":
    
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    
    g.add_edge("A", "B", 2)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "C", 1)
    
    # print(g.adjacency)
    print(g.get_edge_weight("A", "B"))
    print(g.get_edge_weight("B", "A"))
    print(g.get_edge_weight("A", "C"))
    print(g.get_edge_weight("B", "C"))