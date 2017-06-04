#author: Xin Shen
#hw1 Q3
#graph in dictionary representation
#complexity O(m+n)
class traversal:
    def __init__(self,graph):
        self.graph = graph
        self.visited = set()
        self.parent = {}
        self.index = {}
        self.min_index = 0
        for n in g:
            self.parent[n] = None
            self.index[n] = -1
    
    def complete_traversal(self, u):
        self.visited.add(u)
        self.index[u] = self.min_index
        for v in self.graph[u]:
            if v not in self.visited:
                self.parent[v] = u
                print("traverse from "+ u + " to " + v) 
                self.complete_traversal(v)
                print("traverse from "+ v + " to " + u)
            if v in self.visited and self.index[v] < self.index[u] and self.parent[v] != u:
                print("traverse from "+ u + " to " + v) 
                print("traverse from "+ v + " to " + u)

g = {"a":{"b","c","d"}, "b":{"a","e"}, "c":{"a"}, "d":{"a","e"}, "e":{"b","d"}}
t = traversal(g)
t.complete_traversal("a")


        
    
