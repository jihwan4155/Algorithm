def enq(v):
    global last
    last += 1
    tree[last] = v

    c = last
    p = c//2
    while p and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2


T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (n+1)
    last = 0

    for i in range(n):
        enq(arr[i])

    sum = 0
    while True: # 자식 노드는 i * 2 , i *2 + 1이기 때문에 //2를 하면 조상 노드들 나옴
        n //= 2
        sum += tree[n]
        if n == 0:
            break

    print(f'#{t}', sum)