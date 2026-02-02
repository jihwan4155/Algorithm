T = int(input())

for t in range(1, T+1): # 테스트 케이스 개수 순회
    N, M = map(int, input().split()) 
    arr = list(map(int, input().split()))
    max_ = 0
    min_ = sum(arr[0: M]) # 최소값은 첫번째 구간 합으로 초기화
    for i in range(0, N-M+1): # 최대 index 전까지만 검사
        val = sum(arr[i:i+M])  # 구간 합 구하기
        if val > max_:
            max_ = val
        elif val < min_:
            min_ = val

    print(f'#{t} {max_ - min_}')