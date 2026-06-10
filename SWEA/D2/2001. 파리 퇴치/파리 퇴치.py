T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    ans = 0
    for j in range(N-M+1):
        for i in range(N-M+1):
            flys = 0
            for k in range(M):
                flys += sum(arr[j+k][i:i+M])
            
            ans = max(flys, ans)

    print(f'#{tc} {ans}')