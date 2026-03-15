def order(v):
    global num
    if v > n:
        return
    order(v*2)
    tree[v] = num
    num += 1
    order(v*2+1)
    

T = int(input())
for t in range(1, T+1):
    n = int(input())
    tree = [0] * (n+1)
    num = 1
    order(1)
    print(f'#{t}', tree[1], tree[n//2])