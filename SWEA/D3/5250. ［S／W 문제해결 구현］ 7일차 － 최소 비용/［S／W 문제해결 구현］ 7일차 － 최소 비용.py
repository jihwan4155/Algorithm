import heapq

def dijkstra(first):
    dist = [[float('inf')] * n for _ in range(n)]
    hq = []
    dist[first[0]][first[1]] = 0
    heapq.heappush(hq, (0, first))

    while hq:
        distance, node = heapq.heappop(hq)

        if dist[node[0]][node[1]] < distance:
            continue

        for y, x in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            dy = node[0] + y
            dx = node[1] + x
            if 0 <= dy < n and 0 <= dx < n:
                high = 0
                if arr[node[0]][node[1]] < arr[dy][dx]:
                    high = arr[dy][dx] - arr[node[0]][node[1]] 
                
                weight = distance + high + 1

                if weight < dist[dy][dx]:
                    dist[dy][dx] = weight
                    heapq.heappush(hq, (weight, (dy, dx)))
        
    return dist


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    start = (0, 0)
    ret = dijkstra(start)

    print(f'#{tc}', ret[n-1][n-1])