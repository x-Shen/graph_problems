import queue
from math import inf

# use adjacent list to represent graphs

class Flow:
    def __init__(self,graph):
        self.graph = graph
        self.nodes_count = len(graph)

    def bfs(self, s, t, parent):
        # return if there's a path between s and t, and save path in parent
        visited = [False]*self.nodes_count
        #print(visited)
        q = queue.Queue()
        q.put(s)
        visited[s] = True

        while q.empty() != True:
            u = q.get()
            #print(self.nodes_count)
            for ind, val in enumerate(self.graph[u]):
                #print(n)
                if visited[ind] == False and val > 0:
                    q.put(ind)
                    visited[ind] = True
                    parent[ind] = u
        return visited[t]

    def fordFulkerson(self, source, sink):
        #use bfs to save path 
        parent = [-1]*self.nodes_count
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = inf
            s = sink
            while s != source:
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
                if v==source:
                    break
        return max_flow

graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
f = Flow(graph)
flow = f.fordFulkerson(0,5)
print(flow)
        
                
