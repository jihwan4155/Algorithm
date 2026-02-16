T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    for _ in range(m):
        i, j = map(int, input().split())
        # 중심 a[i-1]
        for k in range(1, j+1):
            left = i-1-k
            right = i-1+k
            if 0 <= left < n and 0 <= right < n:
                if a[left] == a[right]:
                    if a[left] == 1:
                        a[left], a[right] = 0, 0
                    else:
                        a[left], a[right] = 1, 1
            else:
                break
    print(f'#{t}', *a)