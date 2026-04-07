import heapq, math

def dijkstra(v):
    distance = [math.inf] * (n+1)
    distance[v] = 0
    hq = [(0, v)]
    
    while hq:
        weight, node = heapq.heappop(hq)
        if distance[node] < weight:
            continue
        for dis, adj in road[node]:
            dist = weight + dis
            if dist < distance[adj]:
                heapq.heappush(hq, (dist, adj))
                distance[adj] = dist
   
    return distance

T = int(input())
for t in range(1, T+1):
    n, e = map(int, input().split()) # n 노드, e 간선
    road = [[] for _ in range(n+1)]
    for i in range(e):
        s, e, w = map(int, input().split())
        road[s].append((w, e)) # 거리, 도착
    
    way = dijkstra(0)
    print(f'#{t}', way[n])