import math, heapq

def dijkstra(v):
    second = [math.inf] * 100001
    min_heap = []
    second[v] = 0
    heapq.heappush(min_heap, (0, v)) # 점, 거리
    while min_heap:
        sec, cur = heapq.heappop(min_heap)
        if sec > second[cur]:
            continue
    
        # -1
        x = cur - 1
        if 0 <= x <= 100000 and sec + 1 < second[x]:
            second[x] = sec + 1
            heapq.heappush(min_heap, (sec + 1, x))

        # +1
        x = cur + 1
        if 0 <= x <= 100000 and sec + 1 < second[x]:
            second[x] = sec + 1
            heapq.heappush(min_heap, (sec + 1, x))

        # *2 (0초)
        x = cur * 2
        if 0 <= x <= 100000 and sec < second[x]:
            second[x] = sec
            heapq.heappush(min_heap, (sec, x))

    return second[k]
    

n, k = map(int, input().split())

print(dijkstra(n))
