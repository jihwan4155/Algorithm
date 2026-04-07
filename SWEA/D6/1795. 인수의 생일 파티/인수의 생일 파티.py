import heapq, math

def dijkstra(v):
    distance = [math.inf] * (N+1)
    distance[v] = 0
    hq = [(0, v)]
    while hq:
        weight, node = heapq.heappop(hq)
        if distance[node] < weight:
            continue
        if v != X and node == X:
            break
        
        for dis, next in graph[node]:
            dist = weight + dis
            if dist < distance[next]:
                heapq.heappush(hq, (dist, next))
                distance[next] = dist
    return distance
    
T = int(input())
for t in range(1, T+1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append((c, y)) # 거리, 도착 노드
    
    from_x = dijkstra(X)
    ret = 0
    
    for i in range(1, N+1):
        if i == X:
            continue
        to_x = dijkstra(i)
        if to_x[X] + from_x[i] > ret:
            ret = to_x[X] + from_x[i]
    
    print(f'#{t}', ret)