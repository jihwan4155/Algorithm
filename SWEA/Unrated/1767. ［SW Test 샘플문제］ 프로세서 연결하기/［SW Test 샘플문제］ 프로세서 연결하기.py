dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def connect(idx, dir, board):
    check = [row[:] for row in board]
    longs = 0
    while True:
        dr = dy[dir] + idx[0]
        dc = dx[dir] + idx[1]
        if 0 <= dr < n and 0 <= dc < n:
            if check[dr][dc] == 2 or check[dr][dc] == 1:
                return None, 0
            check[dr][dc] = 2
            idx = (dr, dc)
            longs += 1
        else:
            return check, longs


# 4 방향으로 가다가 전선은 2로 고정해서, 
# 만약 1이나 2있으면 return
def delta(index, line, con, grid):
    global length, c, core_num
    if index == core_num:
        if con > c:
            c = con
            length = line
        elif con == c: 
            length = min(length, line)
        return

    y, x = core[index]

    for d in range(4):
        new_grid , le = connect((y, x), d, grid)
        if new_grid:
            delta(index+1, line+le, con+1, new_grid)

    delta(index+1, line, con, grid)

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 가장 자리에 있으면 이미 연결된 것 (0 or n)
    # 최대한 많은 core에 전원 연결 -> 전선의 길이의 합
    # 여러 방법이 있으면 전선길이 최소
    # 연결 안되는 core 있을 수도 있음

    core = []
    core_num = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                if not(i == 0 or j == 0 or i == n-1 or j == n-1):
                    core.append((i, j))
                    core_num += 1

    visited = [row[:] for row in arr]
    length, c = 0, 0 
    delta(0, 0, 0, visited)
    print(f'#{t}', length)