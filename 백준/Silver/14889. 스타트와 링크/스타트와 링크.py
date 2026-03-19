def form(t1, v1, t2, prev, dif):
    global diff
    if len(t1) == n//2:
        t2 = []
        v2 = 0

        for i in range(1, n+1):
            if i not in t1:
                t2.append(i)

        for i in range(n//2-1):
            for j in range(i+1, n//2):
                v2 += arr[t2[i]-1][t2[j]-1] + arr[t2[j]-1][t2[i]-1]
        
        diff = min(abs(v1-v2), diff)
        return
    
    for i in range(prev + 1, n+1):
        t1.append(i)
        val1 = v1

        if len(t1) >= 0:
            for j in t1:
                val1 += arr[j-1][i-1] + arr[i-1][j-1]
                
        form(t1, val1, t2, i, dif)
        t1.pop()
        

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
diff = 99 * n

form([], 0, [], 0, diff)
print(diff)