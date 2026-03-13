def sub_set(lst, prev):
    global ans

    if sum(lst) >= b and sum(lst) < ans:
        ans = sum(lst)
        return
    
    if len(lst) == n:
        return

    for i in range(prev + 1, n):
        if used[i] == 1:
            continue
        lst.append(s[i])
        used[i] = 1
        sub_set(lst, i)
        lst.pop()
        used[i] = 0

T = int(input())
for t in range(1, T+1):
    # 부분집합을 구해 그 중에 b 이상인 탑을 구하고 그 중에 최소값 구하기
    # Hi <= 10000
    n, b = map(int, input().split())
    s = list(map(int, input().split()))
    used = [0] * n
    ans = sum(s)
    sub_set([], -1)
    print(f'#{t} {ans - b}')