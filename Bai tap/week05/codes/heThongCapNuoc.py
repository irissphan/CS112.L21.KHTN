import io, os, collections

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def breadth_first_search(graph, root): 
    visited, queue = set(), collections.deque([root])
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited

graph = collections.defaultdict(list)
visited = set()

if __name__ == '__main__':
    n, m = map(int, input().decode().split())
    visit = set()
    
    for _ in range(m):
        a, b = input().decode().split()
        if int(a) < 1 or int(b) < 1: continue
        if int(a) > n or int(b) > n: continue
        graph[a].append(b) if b not in graph[a] else None
        graph[b].append(a) if a not in graph[b] else None

    res, cnt, c = 1, 0, 0
    for u in graph:
        if u in visit: continue
        cnt += 1
        visited = breadth_first_search(graph, u)
        visit.update(visited)
        c += len(visited)
        res *= len(visited)

    print(n - c + cnt - 1)
    print((res * n**(n - c + cnt - 2)) % (10**9 + 7) if n - c + cnt - 1 > 0 else 0)