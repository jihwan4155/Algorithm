def find_set(x):
    if par[x] == x:
        return x
    
    return find_set(par[x])

def union_set(x, y):
    p1 = find_set(x)
    p2 = find_set(y)

    par[p2] = p1


T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    par = [i for i in range(n+1)]

    for i in range(m):
        s1, s2 = arr[i*2], arr[i*2+1]
        union_set(s1, s2)
    
    ans = set()
    for i in range(1, n+1):
        a = find_set(i)
        ans.add(a)
    
    print(f'#{tc}', len(ans))