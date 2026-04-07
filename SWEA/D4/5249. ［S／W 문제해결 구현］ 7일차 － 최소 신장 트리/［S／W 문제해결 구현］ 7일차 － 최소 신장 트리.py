import heapq
def prim(start):
    hq = [(0, start)]
    visited = [0] * (v+1)
    min_weight = 0
    
    while hq:
        weight, node = heapq.heappop(hq)
        if visited[node]:
            continue
        
        visited[node] = 1
        min_weight += weight
        
        for w, next in graph[node]:
            if not visited[next]:
                heapq.heappush(hq, (w, next))
                
    return min_weight


T = int(input())
for t in range(1, T+1):
    # 0 - V 노드, E 간선
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        graph[n1].append((w, n2))
        graph[n2].append((w, n1))
    
    print(f'#{t}', prim(0))