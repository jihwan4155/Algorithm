import heapq

def prim(v):
    ans = 0
    visited = [0] * (V+1)
    q = []
    heapq.heappush(q, (0, v))

    while q:
        weight, n = heapq.heappop(q)
        if visited[n]:
            continue
        visited[n] = 1
        ans += weight
        for nd, distance in node[n]:
            if visited[nd]:
                continue
            heapq.heappush(q, (distance, nd))
    
    return ans


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        node[n1].append((n2, w))
        node[n2].append((n1, w))
    
    ret = prim(0)
    print(f'#{tc}', ret)
