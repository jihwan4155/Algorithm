for t in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    count = 0
    for row in range(100):
        for col in range(100):
            if arr[row][col] == 1:
                drow = row + 1
                # 아래로 내린다. row + 1
                while drow < 100:
                    # 2 만나면 카운팅 후 break
                    if arr[drow][col] == 2:
                        count += 1
                        break
                    # 1 만나면 브레이크
                    elif arr[drow][col] == 1:
                        break
                    # 아무것도 못만나면 계속 내려감
                    else:
                        drow += 1
                        continue
    print(f'#{t} {count}')