import heapq

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    hq = []
    ret = []
    for _ in range(N):
        cmd = list(input().split())
        if len(cmd) != 1:
            heapq.heappush(hq, int(cmd[-1]) * -1)
        else:
            if len(hq) == 0:
                ret.append(-1)
            else:
                x = abs(heapq.heappop(hq))
                ret.append(x)
    
    print(f'#{tc}', *ret)