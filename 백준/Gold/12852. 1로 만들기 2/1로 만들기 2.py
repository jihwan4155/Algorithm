x = int(input())

dp = [0] * (x + 1) # 최소 계산 횟수 카운트 
prev = [0] * (x + 1) # 이동 idx

for i in range(2, x + 1):
    dp[i] = dp[i-1] + 1 # 기본은 -1 
    prev[i] = i-1 # -1 된 값으로 이동 idx

    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1 # 2로 나눈 수보다 1번 더 계산
        prev[i] = i//2 # 2로 나눈 수로 이동 idx

    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        prev[i] = i//3

# 경로 추적
path = []
cur = x
while cur:
    path.append(cur)
    cur = prev[cur]

print(dp[x])
print(*path)
