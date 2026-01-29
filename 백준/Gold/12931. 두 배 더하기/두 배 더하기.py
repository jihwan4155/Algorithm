N = int(input())

A = [0 for _ in range(N)]
B = list(map(int, input().split()))

cnt = 0

while True:
 
    for num in range(N):
        if B[num] % 2 != 0:
            B[num] -= 1
            cnt += 1

    if sum(B) == 0:
        break
    
    is_even = True
    for x in B:
        if x % 2 != 0:
            is_even = False
            break
    
    if is_even:
        for num in range(N):
            if B[num] != 0:
                B[num] //= 2
        cnt += 1


print(cnt)