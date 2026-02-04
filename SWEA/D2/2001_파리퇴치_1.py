T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    def in_range(x, y): # 유효 인덱스 판별 함수
        return 0 <= x < N and 0 <= y < N

    ret = 0
    for i in range(N): # 기준점 행 인덱스
        for j in range(N): # 기준점 열 인덱스
            total = 0
            for k in range(M): # 열 인덱스 돌리기
                y = i + k
                x = j + M
                if in_range(x - 1, y): # 유효한 인덱스인가?
                    total += sum(arr[y][j:x]) # 맞다면 슬라이싱으로 열의 합
                else: # 유효하지 않다면 다음 기준점으로
                    break
            else: # 모두 유효한 인덱스로 break 걸리지 않았다면
                if ret < total: # 최대값 비교 및 초기화
                    ret = total
    print(f'#{t} {ret}')
