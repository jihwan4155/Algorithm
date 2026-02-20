def in_order(v):
    if v <= n:
        in_order(2*v)
        ans.append(tree[v])
        in_order(2*v+1)


T = 10
for t in range(1, T+1):
    n = int(input())
    tree = [''] * (n+1)
    for _ in range(n):
        temp = input().split()
        idx = int(temp[0])
        tree[idx] = temp[1]
        
    ans = []
    in_order(1)

    print(f'#{t}', ''.join(ans))
