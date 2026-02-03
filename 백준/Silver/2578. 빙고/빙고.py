arr = [list(map(int, input().split())) for _ in range(5)]

call = []

for _ in range(5):
    x = list(map(int, input().split()))
    call.extend(x)

def check_bingo():
    bingo = 0

    for i in range(5):
        if arr[i][0:5] == [0] * 5:
            bingo += 1

    for j in range(5):
        column = [row[j] for row in arr]
        if column == [0] * 5:
            bingo += 1

    for k in range(5):
        if arr[k][4-k] != 0:
            break
    else:
        bingo += 1
    
    for p in range(5):
        if arr[p][p] != 0:
            break
    else:
        bingo += 1
    
    return bingo

done = False
times = 0
for c in call:
    times += 1
    for row in range(len(arr)):
        if c in arr[row]:
            b = arr[row].index(c)
            arr[row][b] = 0
            
        if check_bingo() >= 3:
            done = True
            break

    if done:
        print(times)
        break
    