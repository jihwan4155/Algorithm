import heapq

T = int(input())
for t in range(1, T+1):
    n = int(input())
    node = list(map(int, input().split()))

    min_heap = []
    for i in node:
        heapq.heappush(min_heap, i)

    last = n-1
    ans = 0
    while last > 0:
        last = (last-1)//2
        ans += min_heap[last]

    print(f'#{t}', ans)