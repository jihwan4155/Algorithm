def dfs(v, lst):
    global cnt

    if lst:
        if lst[-1] == g:
            cnt += 1
            return
    
    for w in graph[v]:
        if w not in lst:
            lst.append(w)
            dfs(w, lst)
            lst.pop()

T = int(input())
for t in range(1, T+1):
    n, e = map(int, input().split())
    way = list(map(int, input().split()))
    s, g = map(int, input().split())
    
    graph = [[] for _ in range(n+1)]
    
    for i in range(e):
        start, end = way[i*2], way[i*2+1]
        graph[start].append(end)
    
    visited = [0] * (n+1)
    cnt = 0
    dfs(s, [])
    print(f'#{t}', cnt)    