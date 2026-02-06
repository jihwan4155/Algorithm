N = int(input())
time = list(map(int, input().split()))

sorted_lst = sorted(time)

total = 0
for i in range(len(sorted_lst)):
    total += sorted_lst[i] * (len(sorted_lst) - i) 

print(total)