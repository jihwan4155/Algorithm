def subset(total, cnt, prev):
    global ans
    if total > k:
        return
    if cnt > n:
        return

    if cnt == n and total == k:
        ans += 1
    
    for i in range(prev+1, 13):
        subset(total+i, cnt+1, i)


T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    ans = 0
    subset(0, 0, 0)
    print(f'#{t}', ans)