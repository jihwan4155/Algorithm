T = int(input())

for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]

    cnt = 0
    for i in range(n//2):
        cnt += sum(arr[i][n//2-i:n//2+i+1])
        cnt += sum(arr[-(i+1)][n//2-i:n//2+i+1])
    
    cnt += sum(arr[n//2])
    
    print(f'#{t}', cnt)