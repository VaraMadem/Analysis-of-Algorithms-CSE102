#!/usr/local/bin/python3
# your python code starts here
import sys

# Open file
infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

# Parse sizes
vert_count = int(infile.readline())
edge_count = int(infile.readline())

# Parse edges
edges = []
for i in range(edge_count):
    # Append (label, u, v, weight)
    edges.append(tuple([i+1] + [int(d) for d in infile.readline().split()]))

# Sort edges by weight
edges = sorted(edges, key= lambda x: x[3])

# Create parent list, and rank for optimization
parent = [v for v in range(vert_count)]
rank = [0]*vert_count

def find(x):
    """Find representative for x's disjoint set"""
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):
    """Union x and y's disjoint set"""
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[y] > rank[x]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x] += 1

# MWST Algorithm
MWST = []
i = 0
e = 0
while e < vert_count - 1:
    l, v1, v2, w = edges[i]
    i += 1

    x = find(v1-1)
    y = find(v2-1)
    if x != y:
        MWST.append((l, v1, v2, w))
        e += 1
        union(x, y)

total = 0
outbuf = ''
for l,u,v,w in MWST:
    outbuf += f"{' '*(3-l//10)+str(l)}: ({u}, {v}) {format(w, '.1f')}\n"
    total += w

outbuf += f"Total Weight = {format(total, '.2f')}\n"
outfile.write(outbuf)
