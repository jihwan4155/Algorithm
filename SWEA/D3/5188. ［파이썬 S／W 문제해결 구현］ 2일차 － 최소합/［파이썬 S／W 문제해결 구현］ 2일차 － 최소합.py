drs = [1, 0]
dcs = [0, 1]
def move(r, c, val):
    global ans

    if val > ans:
        return

    if r == n-1 and c == n-1:
        if val < ans:
            ans = val
        return
    
    for d in range(2):
        dy = r + drs[d]
        dx = c + dcs[d]
        if 0 <= dy < n and 0 <= dx < n:
            move(dy, dx, val+arr[dy][dx])


T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 10 * (n*2-1)
    move(0, 0, arr[0][0])
    print(f'#{t}', ans)