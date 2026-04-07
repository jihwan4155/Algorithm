import heapq, math

def dijkstra(v, arr):
    distance = [math.inf] * (N+1)
    distance[v] = 0
    hq = [(0, v)]
    while hq:
        weight, node = heapq.heappop(hq)
        if distance[node] < weight:
            continue
        if v != X and node == X:
            break
        
        for dis, next in arr[node]:
            dist = weight + dis
            if dist < distance[next]:
                heapq.heappush(hq, (dist, next))
                distance[next] = dist
    return distance
    
T = int(input())
for t in range(1, T+1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    back_graph = [[] for _ in range(N+1)] # 돌아오는 것은 가는 거 반대
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append((c, y)) # 거리, 도착 노드
        back_graph[y].append((c, x)) 
    
    from_x = dijkstra(X, graph)
    to_x = dijkstra(X, back_graph)
    ret = 0
    
    for i in range(1, N+1):
        if i == X:
            continue
        ret = max(ret, from_x[i] + to_x[i])
    
    print(f'#{t}', ret)