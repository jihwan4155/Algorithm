T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 마지막 N비트가 모두 1인 마스크 생성
    mask = (1 << N) - 1

    # M에서 마지막 N비트 뽑은 결과가 MASK와 같은지 확인
    if (M & mask) == mask:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')