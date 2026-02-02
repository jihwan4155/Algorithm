T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_val = 0 # 최대값
    for i in range(N):
        check = 0 # 인덱스별 값 확인
        for j in range(i, N):
            if arr[i] > arr[j]: # 다음 인덱스의 수가 작으면
                check += 1 # 공간 + 1
        if check > max_val: # 최대 공간 체크
            max_val = check
    print(f'#{t} {max_val}')