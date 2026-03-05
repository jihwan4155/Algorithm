from collections import deque

def bfs(v):
    visited = [0] * (n+1)
    visited[v] = 1
    q = deque()
    q.append(v)

    num = 0
    while q:
        computer = q.popleft()
        num += 1
        for i in relationship[computer]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    hack[v] = num

n, m = map(int, input().split())
relationship = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    relationship[b].append(a)



hack = [0] * (n+1)
ans = []

for j in range(1, n+1):
    if relationship[j]:
        bfs(j)

max_n = max(hack)
for i in range(1, n+1):
    if max_n == hack[i]:
        ans.append(i)

print(*ans)