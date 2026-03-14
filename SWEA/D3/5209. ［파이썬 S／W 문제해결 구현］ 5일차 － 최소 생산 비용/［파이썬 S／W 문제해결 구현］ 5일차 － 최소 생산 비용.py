
def dfs(cnt, total):
    global ans
    global n
    if cnt == n:
        if total < ans:
            ans = total
        return

    for i in range(n):
        if used[i]:
            continue
        if total > ans:
            continue
        used[i] = 1
        dfs(cnt + 1, total + arr[cnt][i])
        used[i] = 0


T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    used = [0] * n
    ans = 9876543210
    dfs(0, 0)
    print(f'#{t}', ans)
