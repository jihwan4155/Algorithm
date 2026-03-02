drs = [0, 0, -1, 1]
dcs = [1, -1, 0, 0]

def dfs(r, c):
    visited[r][c] = 1
    if arr[r][c] == '3':
        return

    for d in range(4):
        dy = r + drs[d]
        dx = c + dcs[d]
        if 0 <= dy < 16 and 0 <= dx < 16 and visited[dy][dx] != 1 and arr[dy][dx] != '1':
            dfs(dy, dx)

for _ in range(10):
    t = int(input())
    arr = [input() for _ in range(16)]
    start_r, start_c = 0, 0
    end_r, end_c = 0, 0
    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                start_r, start_c = i, j
            elif arr[i][j] == '3':
                end_r, end_c = i, j
    
    visited = [[0]*16 for _ in range(16)]

    dfs(start_r, start_c)
    if visited[end_r][end_c] == 1:
        print(f'#{t}', 1)
    else:
        print(f'#{t}', 0)
