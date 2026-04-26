from collections import deque

def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                q.append((i, j))
    
    while q:
        y, x = q.popleft()
        for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            dr, dc = y + dy, x + dx
            if 0 <= dr < n and 0 <= dc < m and arr[dr][dc] == 'L':
                if visited[dr][dc] == 0:
                    visited[dr][dc] = visited[y][x] + 1
                    q.append((dr, dc))
                    

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    
    bfs()
    cnt = 0
    for row in visited:
        cnt += sum(row)
    
    print(f'#{tc} {cnt}')
