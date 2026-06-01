T = int(input())

for tc in range(1, T+1):
    X = int(input())
    ans = ''

    if X == 1:
        ans = '0'
    elif X % 2 == 0:
        ans = X//2 * '8'
    else:
        ans = '4' + '8' * ((X - 1) // 2)

    print(f'{ans}')
