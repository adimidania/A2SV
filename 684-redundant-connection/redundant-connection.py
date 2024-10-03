class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def findRedundantConnection(self, edges):
        uf = UnionFind(len(edges) + 1)  
        redundant_edge = []

        for u, v in edges:
            if uf.find(u) == uf.find(v):
                redundant_edge = [u, v] 
            else:
                uf.union(u, v)  

        return redundant_edge 