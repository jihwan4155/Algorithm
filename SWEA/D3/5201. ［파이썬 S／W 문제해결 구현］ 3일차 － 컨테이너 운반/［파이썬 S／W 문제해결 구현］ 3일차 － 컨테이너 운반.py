T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    container = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    container.sort(reverse=True)
    trucks.sort(reverse=True)

    idx = 0
    flag = False
    weight = 0
    for i in range(m):
        for j in range(idx, n):
            if trucks[i] >= container[j]:
                weight += container[j]
                idx = j + 1
                if j + 1 > m:
                    flag = True
                break
        else:
            flag = True

        if flag:
            break
    
    print(f'#{t}', weight)