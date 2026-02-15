def bfs(start, end):
    visited = [-1] * (v+1)
    q = [start]
    visited[start] = 0
    while q:
        num = q.pop(0)
        if num  == end:
            print(f'#{t}',visited[num])
            return

        for i in way[num]:
            if visited[i] == -1:
                visited[i] = visited[num] + 1
                q.append(i)
    print(f'#{t}', 0)
    return 

T = int(input())
for t in range(1, T+1):
    v, e = map(int, input().split())
    way = [[] for _ in range(v+1)]

    for i in range(e):
        x, y = map(int, input().split())
        way[x].append(y)
        way[y].append(x)
    
    s, g = map(int, input().split())

    bfs(s, g) 