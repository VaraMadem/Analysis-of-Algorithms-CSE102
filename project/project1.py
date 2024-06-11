import sys

class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

def kruskal(n, edges):
    uf = UnionFind(n)
    mst = []
    edges.sort(key=lambda e: e[2])
    for u, v, weight, label in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight, label))
            if len(mst) == n-1:
                break
    return mst

def read_graph(input_file):
    with open(input_file, 'r') as file:
        n = int(file.readline().strip())
        m = int(file.readline().strip())
        edges = []
        for i in range(m):
            u, v, w = map(int, file.readline().strip().split())
            edges.append((u-1, v-1, w, i+1))
    return n, edges

def write_output(output_file, mst):
    with open(output_file, 'w') as file:
        total_weight = sum([w for _, _, w, _ in mst])
        for u, v, weight, label in sorted(mst, key=lambda x: x[3]):
            file.write(f'{label:>4}: ({u+1}, {v+1}) {weight:.1f}\n')
        file.write(f'Total Weight = {total_weight:.2f}\n')

def main(input_file, output_file):
    n, edges = read_graph(input_file)
    mst = kruskal(n, edges)
    write_output(output_file, mst)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: MWST <input_file> <output_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
