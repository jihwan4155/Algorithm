
def battery(stop):
    global cnt
    if stop == 1:
        return
    
    for i in range(1, stop):
        if stop - i <= stops[i]:
            stop = i
            cnt += 1
            break
    
    battery(stop)
    

T = int(input())
for t in range(1, T+1):
    stops = list(map(int, input().split()))

    cnt = 0
    battery(stops[0])
    print(f'#{t}', cnt-1)