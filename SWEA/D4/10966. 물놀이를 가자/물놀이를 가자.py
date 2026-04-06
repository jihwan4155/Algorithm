from collections import deque
def bfs():
    visited = [[0]*m for _ in range(n)]
    q = deque()
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                q.append((i, j))
                visited[i][j] = 1
    
    while q:
        y, x = q.popleft()
        for dy, dx in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            dr = dy + y
            dc = dx + x
            if 0 <= dr < n and 0 <= dc < m and not visited[dr][dc]:
                distance[dr][dc] = distance[y][x] + 1
                visited[dr][dc] = 1
                q.append((dr, dc))
    
                    
T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    cnt = 0
    distance = [[0]*m for _ in range(n)]
    bfs()
    
    for row in range(n):
        cnt += sum(distance[row])
    
    print(f'#{t}', cnt)