import heapq

def dijkstra(start):
    distance = [float('inf')] * (n+1)
    hq = [(0, start)]
    while hq:
        weight, node = heapq.heappop(hq)
        if distance[node] < weight:
            continue
        for dist, next in graph[node]:
            d = dist + weight
            if d < distance[next]:
                heapq.heappush(hq, (d, next))
                distance[next] = d
    
    return distance[n]


T = int(input())
for tc in range(1, T+1):
    n, e = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(e):
        s, end, w = map(int, input().split())
        graph[s].append((w, end))
    
    ret = dijkstra(0)
    print(f'#{tc} {ret}')