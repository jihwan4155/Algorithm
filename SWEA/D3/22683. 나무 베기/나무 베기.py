import heapq

dy = [-1, 0, 1, 0] # 북 동 남 서
dx = [0, 1, 0, -1]

def bfs(s, cut):
    cnt = [[[[float('inf')] * (cut+1) for _ in range(4)] for _ in range(n)] for _ in range(n)]
    q = []
    for d in range(4):
        cnt[s[0]][s[1]][d][0] = 0
    heapq.heappush(q, (0, s, 0, 0))

    while q:
        cost, axis, c, dir = heapq.heappop(q)
        y, x = axis[0], axis[1]

        if y == end[0] and x == end[1]:
            return cost
        
        if cnt[y][x][dir][c] < cost:
            continue

        for i in range(4):
            dr = y + dy[i]
            dc = x + dx[i]
            if 0 <= dr < n and 0 <= dc < n:
                nc = c
                if arr[dr][dc] == 'T':
                    if nc + 1 <= cut:
                        nc += 1
                    else:
                        continue
                
                turn = min(abs(dir - i), 4 - abs(dir - i))
                new_cost = cost + turn + 1

                if new_cost < cnt[dr][dc][i][nc]:
                    cnt[dr][dc][i][nc] = new_cost
                    heapq.heappush(q, (new_cost, (dr, dc), nc, i))

    return -1


# 앞으로 이동, 좌/우 회전 
T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split()) # n 배열 크기, k 나무 베기
    arr = [input() for _ in range(n)] # str 타입
    # G 땅, T 나무, X 차 위치, Y 도착
    start, end = (0, 0), (0, 0)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':
                start = (i, j)
            elif arr[i][j] == 'Y':
                end = (i, j)
    
    ans = bfs(start, k)
    print(f'#{t}', ans)
