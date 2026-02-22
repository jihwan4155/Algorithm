def max_profit(idx, prf):
    len = con[idx][0] + idx
    if len > n:
        return
    prf += con[idx][1]
    max_v = prf
    for k in range(len, n):
        if con[k][0] == 0:
            continue
        max_v = max(max_v, max_profit(k, prf))

    return max_v

n = int(input())
con = [[0, 0] for _ in range(n)]
for i in range(n):
    t, p = map(int, input().split())
    if i + t > n:
        continue
    con[i][0] = t
    con[i][1] = p

ret = 0
for j in range(n):
    check = max_profit(j, 0)
    if check > ret:
        ret = check
print(ret)