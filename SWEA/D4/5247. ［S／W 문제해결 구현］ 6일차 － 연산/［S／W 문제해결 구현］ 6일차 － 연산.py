
from collections import deque


def dps(v, end):
    dp[v] = 0

    q = deque()
    q.append(v)

    while q:
        t = q.popleft()
        if t == end:
            return dp[t]
        for i in range(4):
            if i == 0:
                if 1 <= t+1 <= 1000000 and dp[t+1] == -1:
                    dp[t+1] = dp[t] + 1
                    q.append(t+1)

            elif i == 1:
                if 1 <= t-1 <= 1000000 and dp[t-1] == -1:
                    dp[t-1] = dp[t] + 1
                    q.append(t-1)

            elif i == 2:
                if 1 <= t*2 <= 1000000 and dp[t*2] == -1:
                    dp[t*2] = dp[t] + 1
                    q.append(t*2)
            
            else:
                if 1 <= t-10 <= 1000000 and dp[t-10] == -1:
                    dp[t-10] = dp[t] + 1
                    q.append(t-10)



T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    dp = [-1] * 1000001

    ans = dps(n, m)

    print(f'#{tc}', ans)