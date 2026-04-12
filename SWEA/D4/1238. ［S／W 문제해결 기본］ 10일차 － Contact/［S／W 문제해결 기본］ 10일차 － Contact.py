from collections import defaultdict, deque

def bfs(p):
    visited[p] = 0
    q = deque()
    q.append(p)
    while q:
        x = q.popleft()
        for i in contact[x]:
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                q.append(i)


for tc in range(1, 11):
    num, start = map(int, input().split())
    data = list(map(int, input().split()))

    contact = defaultdict(set)
    visited = defaultdict(int)
    for i in range(num//2):
        f, t = data[i*2], data[i*2+1]
        contact[f].add(t)
        visited[f] = -1
        visited[t] = -1
    
    bfs(start)

    cnt = 0
    ans = -1

    for k, v in visited.items():
        if cnt < v:
            cnt = v
            ans = k
        elif cnt == v:
            if k > ans:
                ans = k
    
    print(f'#{tc}', ans)