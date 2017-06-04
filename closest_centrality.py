from queue import PriorityQueue
import math

class closest_centrality:
    
    def __init__(self,graph):
        # graph in python dictionary representation
        self.graph = graph
        
    def dijkstra(self, v):
        d = {}
        pq = PriorityQueue()
        for vertex in self.graph:
            d[vertex] = math.inf
        pq.put((0,v))
        d[v] = 0
        while pq.empty() == False:
            cur_vertex = pq.get()[1]
            for dest in self.graph[cur_vertex]:
                if  d[cur_vertex] + self.graph[cur_vertex][dest]< d[dest]:
                    d[dest] = self.graph[cur_vertex][dest] + d[cur_vertex]
                    pq.put((d[dest],dest))
        return d

    def calculate_centrality(self, v, shortest_paths):
        total_len = sum(shortest_paths.values())
        if total_len == 0:
            return 0
        return 1/total_len


g = {'a':{'b':3, 'c':2, 'e': 10}, 'b':{'a':3,'e':5}, 'c':{'a':2, 'e':5,'d':1},'d':{'c':1},'e':{'a':10,'c':5}}
c = closest_centrality(g)
d = c.dijkstra('a')
print(c.calculate_centrality('a',d))
                
