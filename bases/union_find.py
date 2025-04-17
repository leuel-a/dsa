from collection import Counter

class UnionFind:
    def __init__(self, n: int) -> None:
        self.rank = [1 for _ in range(n)]
        self.parents = [i for i in range(n)]

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            return self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x: int, y: int) -> None:
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent != y_parent:
            x_rank, y_rank = self.rank[x_parent], self.rank[y_parent]

            if x_rank <= y_rank:
                self.parents[x_parent] = y_parent
                self.rank[y_parent] += self.rank[x_parent]
            else:
                self.parents[y_parent] = x_parent
                self.rank[x_parent] += self.rank[y_parent]

    def get_representatives_sizes(self):
        print(Counter(self.parents))

