def dfs(s, dis, lst):
    global num
    num = max(num, dis)

    if dis == n:
        return

    for i in way[s]:
        if i in lst:
            continue
        lst.append(i)
        dfs(i, dis + 1, lst)
        lst.pop()


T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    way = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        way[x].append(y)
        way[y].append(x)
    
    num = 0
    for i in range(1, n+1):
        dfs(i, 1, [i])
    
    print(f'#{t}', num)