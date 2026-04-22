T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mask = 2**10-1 # bin = 1111111111
    check = 0
    idx = 0
    while check < mask: # 1111111111 이 되기 전까지만. 되면 print로
        idx += 1
        x = N * idx
        while x != 0:
            num = x % 10 # 한 자리씩 뽑기
            x //= 10  # 한 자리씩 제거
            check = (1 << num) | check #  지금 나온 숫자 [OR연산] 지금 까지 봤던 숫자 

    print(f'#{tc} {N * idx}')