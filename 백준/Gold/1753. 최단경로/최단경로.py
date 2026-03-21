import math
import heapq

def dijkstra(graph, start_v):
    distance = [math.inf] * (V+1) # 출발 노드에서 각 노드까지 거리 (무제한)
    distance[start_v] = 0 # 출발 노드는 거리 0
    min_heap = []
    heapq.heappush(min_heap, [0, start_v]) # 출발 노드 푸쉬
    while min_heap:
        cur_distance, cur_v = heapq.heappop(min_heap)
        if distance[cur_v] < cur_distance: continue
        # 현재 정점까지의 거리가 이미 갱신된 거리보다 크면 continue
        for next_v, weight in graph[cur_v]: # 다음 도착 노드에서
            dis = cur_distance + weight # 지금 까지 거리 + 다음 노드까지 거리
            if dis < distance[next_v]: # 기존 거리보다 적으면
                distance[next_v] = dis # 초기화
                heapq.heappush(min_heap, [dis, next_v]) # 힙 푸쉬
    return distance

V, e = map(int, input().split()) # v 정점 수, e 간선 수
k = int(input()) # 시작 정점

graph = [[] for _ in range(V+1)]
for i in range(e):
    u, v, w = map(int, input().split()) # u -> v 가중치 w
    graph[u].append((v, w))

ret = dijkstra(graph, k)
for i in range(1, V+1):
    print(str(ret[i]).upper())