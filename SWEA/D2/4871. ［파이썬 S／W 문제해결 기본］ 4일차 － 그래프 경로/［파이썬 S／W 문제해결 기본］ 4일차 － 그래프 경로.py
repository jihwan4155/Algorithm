def dfs(start):
    visited[start] = True
    for w in graph[start]:
        if visited[w] != True:
            dfs(w)

T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    visited = [False] * (V+1)
    graph = [[] for _ in range(V+1)] 
    temp = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    for i in temp:
        graph[i[0]].append(i[1])

    dfs(S)
    if visited[G]:
        print(f'#{t}', 1)
    else:
        print(f'#{t}', 0)