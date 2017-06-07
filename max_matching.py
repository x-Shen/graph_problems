# maximum bipartite matching 
class Graph:
    def __init__(self,graph):
        self.graph = graph
        self.left = len(graph)
        self.right = len(graph[0])

    #dfs to see if a matching for vertex u is possible
    def bpm(self, u, matchR, seen):
        for v in range(self.right):
            if self.graph[u][v] and seen[v] == False:
                seen[v] = True

                if matchR[v] == -1 or self.bpm(matchR[v],matchR, seen):
                    matchR[v] = u
                    return True
        return True

    def maxBPM(self):
        matchR = [-1] * self.right
        result = 0
        for i in range(self.left):
            seen = [False] * self.right
            if self.bpm(i, matchR, seen):
                result+=1
        return result

g = [[0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1]]

bpGraph = Graph(g)
print(bpGraph.maxBPM())
