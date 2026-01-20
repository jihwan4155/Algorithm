arr = [[0] * 101 for _ in range(101)] 

for _ in range(4):
    rect = list(map(int, input().split()))
    # rect = [1, 2, 4, 4]
    for i in range(rect[1], rect[3]):
        for j in range(rect[0], rect[2]):
            arr[-i][j] = 1


sum = 0 

for k in range(101):
    for u in range(101):
        if arr[k][u] == 1:
            sum += 1

print(sum)

