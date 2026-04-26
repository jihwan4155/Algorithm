T = int(input())

def dfs(v, end):
    global cnt 
    visited[v] = True

    if v == end:
        cnt += 1
        return
    
    for w in node[v]:
        if not visited[w]:
            dfs(w, end)
            visited[w] = False



for tc in range(1, T+1):
    N, E = map(int, input().split())
    arr = list(map(int, input().split()))
    S, G = map(int, input().split())

    node = [[] for _ in range(N+1)]
    for i in range(E):
        s, g = arr[i*2], arr[i*2+1]
        node[s].append(g)
    
    visited = [False] * (N+1)

    cnt = 0
    dfs(S, G)

    print(f'#{tc}', cnt)