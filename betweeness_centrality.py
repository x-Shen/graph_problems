# By Xin Shen
import math
from math import inf

# this only work for unique shortest path
# time complexity of this code:
# Floyd-Warshall takes O(n^3), 
# Calcuate centrality O(n^3) for u, for v and reconstruct path takes O(n)
# total complexity: O(n^3)

graph = [[0, 22, 9, 12, inf, inf, inf, inf, inf], 
[22, 0, 35, inf, inf, 36, inf, 34, inf], 
[9, 35, 0, 4, 65, 42, inf, inf, inf], 
[12, inf, 4, 0, 33, inf, inf, inf, 30], 
[inf, inf, 65, 33, 0, 18, 23, inf, inf], 
[inf, 36, 42, inf, 18, 0, 39, 24, inf], 
[inf, inf, inf, inf, 23, 39, 0, 25, 21], 
[inf, 34, inf, inf, inf, 24, 25, 0, 19], 
[inf, inf, inf, 30, inf, inf, 21, 19, 0]]

v = 9

def floyd_washall_with_path(v, graph):
    path = [[None for i in range(v)] for j in range(v)]
    dist = [[math.inf for i in range(v)] for j in range(v)]

    for i in range(v):
        for j in range(v):
            if graph[i][j] != None:
                dist[i][j] = graph[i][j]
                path[i][j] = j
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[i][k]


    return dist, path

def recover_path(u, v, path_mat):
    if path_mat[u][v] == None:
        return []
    path = [u]
    while u != v:
        u = path_mat[u][v]
        path.append(u)
    return path

def calcuate_betweeness_centrality(path_mat,n):
    centrality = 0
    for u in range(len(path_mat)):
        for v in range(len(path_mat)):
            if u != v and n != u and n != v: 
                path = recover_path(u,v,path_mat)
                for node in path:
                    if node == n:
                        #print(path)
                        centrality += 1
                        break
    return centrality
                        
            

        
dist, path = floyd_washall_with_path(9,graph)

for i in range(9):
    print(calcuate_betweeness_centrality(path,i))


