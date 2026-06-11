T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    dp = [0] * (K + 1)

    for _ in range(N):
        v, c = map(int, input().split())

        for weight in range(K, v - 1, -1):
            dp[weight] = max(dp[weight], dp[weight - v] + c)

    print(f'#{tc} {dp[K]}')