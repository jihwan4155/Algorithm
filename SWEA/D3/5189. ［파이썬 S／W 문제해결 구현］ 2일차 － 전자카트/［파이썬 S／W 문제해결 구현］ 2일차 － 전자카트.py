def way(cnt):
    global ans
    if cnt == n:
        battery = 0
        for j in range(n-1):
            battery += arr[lst[j]-1][lst[j+1]-1]
            if battery > ans:
                return
        battery += arr[lst[-1]-1][0]
        if battery < ans:
            ans = battery 
        return
    
    for i in range(2, n+1):
        if used[i]:
            continue
        lst.append(i)
        used[i] = 1
        way(cnt+1)
        lst.pop()
        used[i] = 0


T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    used = [0] * (n+1)
    ans = 0xfffffff
    lst = [1]
    way(1)
    print(f'#{t}', ans)