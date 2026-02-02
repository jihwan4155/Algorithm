T = 10
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    total = 0
    for b in range(2, N-2): # 맨앞 맨뒤 2칸은 제외
        max_v = max(arr[b-2], arr[b-1], arr[b+1], arr[b+2]) # 기준 빌딩 양옆 2칸 중 제일 높은 빌딩
        if arr[b] > max_v: # 양옆 2칸 중 제일 높은 빌딩 보다 큰 세대있으면
            total += arr[b] - max_v # total += 세대수
    print(f'#{t} {total}')
