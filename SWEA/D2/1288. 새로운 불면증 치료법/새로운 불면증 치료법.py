mask = [1] * 10

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    check = [0] * 10

    num = 0
    ans = N
    idx = 1

    flag = False
    while True:
        for i in str(ans):
            if check[int(i)] == 0:
                check[int(i)] = 1
                num += 1
                if num == 10:
                    flag = True
                    break
        
        if flag:
            break

        idx += 1
        ans = N * idx
    
    print(f'#{tc} {ans}')