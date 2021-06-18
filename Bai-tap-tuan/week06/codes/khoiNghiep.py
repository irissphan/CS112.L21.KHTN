import sys, io, os, collections, functools
sys.setrecursionlimit(10**6)
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

class Graph:
    def __init__(self):
        self.time = 0
        self.root = -1
        self.graph = collections.defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def DFS_Visit(self, u, parent, color, d):
        color[u] = 1
        flag = True
        self.time = self.time + 1
        d[u] = self.time
        
        for v in self.graph[u]:
            if not flag:
                return flag
            if color[v] == 2:
                if d[u] < d[v]:
                    # sys.stdout.write('forward edge\n')
                    None
                else:
                    # sys.stdout.write('cross edge\n')
                    if parent[v] != self.root + 1:
                        return False
                    else:
                        parent[v] = u + 1

            elif color[v] == 1:
                # sys.stdout.write('back edge\n')
                return False
    
            else:
                parent[v] = u + 1
                # sys.stdout.write('tree edge\n')
                flag = self.DFS_Visit(v, parent, color, d)

        color[u] = 2
        self.time = self.time + 1

        return flag


def main():
    n, m = map(int, input().split())
    
    parent = [0] * n
    g = Graph()
    
    for _ in range(m):
        u, v = map(int, input().split())
        if u < 1 or v < 1 or u > n or v > n or u == v: continue
        g.addEdge(u-1, v-1)
        parent[v-1] += 1
    
    root = [u for u in range(n) if parent[u] < 1]

    if len(root) < 1 or len(root) > 1:
        sys.stdout.write("No")
        return
    
    g.root = root[0]
    
    d = [0] * n
    color = [0] * n

    is_possible = g.DFS_Visit(g.root, parent, color, d)
    if not is_possible:
        sys.stdout.write("No")
        return
    else:
        parent[g.root] = -1
        sys.stdout.write("Yes\n" + ' '.join(map(str, parent)))
        return

if __name__ == '__main__':
    main()