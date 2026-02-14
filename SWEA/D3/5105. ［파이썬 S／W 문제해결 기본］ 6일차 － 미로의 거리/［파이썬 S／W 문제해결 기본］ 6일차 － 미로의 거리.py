def bfs(graph, vr, vc,):
    visited = [[-1] * n for _ in range(n)]
    queue = [(vr, vc)]
    visited[vr][vc] = 0

    while queue:
        y, x = queue.pop(0)
        for dy, dx in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            rn = dy + y
            cn = dx + x
            if 0 <= rn < n and 0 <= cn < n:
                if visited[rn][cn] == -1 and graph[rn][cn] == '0':
                    visited[rn][cn] = visited[y][x] + 1
                    queue.append((rn, cn))
                    
                elif graph[rn][cn] == '3':
                    print(f'#{t}', visited[y][x])
                    return
    print(f'#{t}', 0)

T = int(input())
for t in range(1, T+1):
    # 1은 벽 # 0은 통로 # 2 출발
    n = int(input())
    arr = [str(input().rstrip()) for _ in range(n)]
    
    r, c = 0, 0
    for j in range(n):
        for i in range(n):
            if arr[j][i] == '2':
                r, c = j, i
                break
    
    bfs(arr, r, c)