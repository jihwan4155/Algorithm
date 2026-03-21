

def dfs(num):
    big_visited = [0] * (n+1)
    less_visited = [0] * (n+1)
    cnt = 0
    stack = [num]
    big_visited[num] = 1
    less_visited[num] = 1

    while stack: # 보다 큰 수들
        t = stack.pop()
        for w in big[t]:
            if big_visited[w] == 0:
                stack.append(w)
                big_visited[w] = 1
                cnt += 1

    stack = [num]
    while stack: # 보다 작은 수들
        t = stack.pop()
        for w in less[t]:
            if less_visited[w] == 0:
                stack.append(w)
                less_visited[w] = 1
                cnt += 1

    return cnt # 자기 자신을 제외하고 비교 가능한 수들의 개수

n = int(input())
m = int(input())
big = [[] for _ in range(n+1)] # 인덱스보다 큰 수
less = [[] for _ in range(n+1)] # 인덱스보다 작은 수
for _ in range(m):
    a, b = map(int, input().split())
    big[b].append(a)
    less[a].append(b)

for i in range(1, n+1):
    print(n-1-dfs(i))