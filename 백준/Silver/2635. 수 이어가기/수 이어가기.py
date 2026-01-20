arr = []

first = int(input())

arr.append(first)

for i in range(1, first+1):
    ex_arr = [first, i]
    cur = i
    while True:
        cur = ex_arr[-2] - ex_arr[-1]
        if cur < 0:
            break
        ex_arr.append(cur)

    if len(ex_arr) > len(arr):
        arr = ex_arr

print(len(arr))
print(*arr)