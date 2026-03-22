import heapq, math

def dijkstra(graph, start, end):
    distances = [math.inf] * (n+1)
    distances[start] = 0
    min_heap = []
    heapq.heappush(min_heap, [0, start])

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        if distances[current_node] < current_distance: continue

        for arrival, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[arrival]:
                distances[arrival] = distance
                heapq.heappush(min_heap, [distance, arrival])

    return distances[end]

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

way = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split()) # 출발, 도착, 비용
    way[s].append((e, w)) # 출발 노드에 도착 노드, 비용 저장


a, b = map(int, input().split())

print(dijkstra(way, a, b))
