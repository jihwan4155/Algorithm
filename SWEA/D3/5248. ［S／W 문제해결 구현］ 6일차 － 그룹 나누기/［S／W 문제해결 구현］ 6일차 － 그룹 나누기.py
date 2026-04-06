def dfs(person):
    stack = [person]
    visited[person] = 1
    
    while stack:
        p = stack.pop()
        for w in node[p]:
            if not visited[w]:
                stack.append(w)
                visited[w] = 1

T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    paper = list(map(int, input().split()))
    node = [[] for _ in range(n+1)]
    for i in range(m):
        x, y = paper[i*2], paper[i*2+1]
        node[x].append(y)
        node[y].append(x)
    
    cnt = 0
    visited = [False] * (n+1)
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    
    print(f'#{t}', cnt)