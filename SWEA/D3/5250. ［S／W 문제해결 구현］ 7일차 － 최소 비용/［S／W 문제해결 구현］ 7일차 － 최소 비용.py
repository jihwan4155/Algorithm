import heapq, math
def dijkstra(r, c):
    distance = [[math.inf]*n for _ in range(n)]
    distance[r][c] = 0 # 시작점 거리 0
    hq = [(0, r, c)]
    
    while hq:
        fuel, row, col = heapq.heappop(hq)
        if distance[row][col] < fuel:
            continue
        for d in [[0, 1], [-1, 0], [0, -1], [1, 0]]:
            dy = row + d[0]
            dx = col + d[1]
            if 0 <= dy < n and 0 <= dx < n:
                altitude = arr[dy][dx]
                exp_fuel = fuel + 1
                if altitude > arr[row][col]:
                    exp_fuel += altitude - arr[row][col]
                # 다음 예상 연료 = 그 전까지 연료 + 높이 차이 (더 높다면) + 기본 연료 1 
                if exp_fuel < distance[dy][dx]:
                    heapq.heappush(hq, (exp_fuel, dy, dx))
                    distance[dy][dx] = exp_fuel
    
    return distance[n-1][n-1]

T = int(input())
for t in range(1, T+1):
    n = int(input())
    # 출발 (0, 0), 도착 (n-1, n-1)
    # 기본 이동 연료 1, 높이 다르면 높이 차이만큼 +
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{t}', dijkstra(0, 0))