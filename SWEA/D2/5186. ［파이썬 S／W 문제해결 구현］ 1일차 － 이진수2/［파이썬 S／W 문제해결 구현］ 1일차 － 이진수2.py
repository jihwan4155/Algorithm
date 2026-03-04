T = int(input())
for t in range(1, T+1):
    n = float(input())

    ret = '0'
    while True:
        if len(ret) > 12:
            print(f'#{t}', 'overflow')
            break
        else:
            n *= 2
            if n >= 1:
                ret += '1'
                n -= 1
            else:
                ret += '0'
            if n == 0:
                print(f'#{t}', ret[1::])
                break