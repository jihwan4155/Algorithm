dcs = [0, 0, 1, -1]
drs = [1, -1, 0, 0]

def bfs(r, c):
    q = [(r, c)]
    visited[r][c] = 1

    while q:
        y, x = q.pop(0)
        if arr[y][x] == '3':
            return 1

        for d in range(4):
            dy = y + drs[d]
            dx = x + dcs[d]
            if 0 <= dy < 100 and 0 <= dx < 100 and visited[dy][dx] == 0 and arr[dy][dx] != '1':
                visited[dy][dx] = 1
                q.append((dy, dx))
    return 0


def dfs(r, c):
    visited[r][c] = 1
    stack = [(r, c)]
    while stack:
        y, x = stack.pop()
        for d in range(4):
            dy = y + drs[d]
            dx = x + dcs[d]
            if 0 <= dy < 100 and 0 <= dx < 100 and visited[dy][dx] == 0 and arr[dy][dx] != '1':
                visited[dy][dx] = 1
                stack.append((dy, dx))
                if arr[dy][dx] == '3':
                    return 1
    return 0
            
for _ in range(10):
    t = int(input())
    arr = [input() for _ in range(100)]
    start = (1, 1)
    visited = [[0] * 100 for _ in range(100)]

    # print(f'#{t}', dfs(start[0], start[1]))
    print(f'#{t}', bfs(start[0], start[1]))
