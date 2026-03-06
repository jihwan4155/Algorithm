drs = [0, 0, 1, -1, -1, -1, 1, 1]
dcs = [1, -1, 0, 0, -1, 1, -1, 1]

def bfs(r, c):
    visited = [[-1]*m for _ in range(n)]
    visited[r][c] = 0
    q = [(r, c)]

    while q:
        y, x = q.pop(0)
        for d in range(8):
            dy = y + drs[d]
            dx = x + dcs[d]
            if 0 <= dy < n and 0 <= dx < m and visited[dy][dx] == -1:
                if arr[dy][dx] == 1:
                    return visited[y][x] + 1
                visited[dy][dx] = visited[y][x] + 1
                q.append((dy, dx))
    return 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

distance = []
for j in range(n):
    for i in range(m):
        if arr[j][i] != 1:
            distance.append(bfs(j, i))

print(max(distance))