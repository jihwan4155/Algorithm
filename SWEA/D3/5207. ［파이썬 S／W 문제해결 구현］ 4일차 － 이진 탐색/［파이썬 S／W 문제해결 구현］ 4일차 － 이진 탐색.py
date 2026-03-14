def binary_search(num, l, r, dir):
    global cnt
    if l > r:
        return

    k = (l+r)//2
    if a[k] == num:
        cnt += 1
        return
    
    if num < a[k]:
        if dir == 1:
            return
        binary_search(num, l, k-1, 1)
    else:
        if dir == 2:
            return
        binary_search(num, k+1, r, 2)
    

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    cnt = 0
    for i in b:
        binary_search(i, 0, n-1, 0)
        # 마지막 0: 방향 변수. 시작 0 왼쪽 1 오른쪽 2
        # 번갈아가면서 봐야하기에 봤던 방향이랑 겹치면 안봄
    print(f'#{t} {cnt}')