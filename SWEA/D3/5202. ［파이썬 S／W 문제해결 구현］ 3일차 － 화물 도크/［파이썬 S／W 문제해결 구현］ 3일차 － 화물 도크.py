def truck(lst, time):
    if time == 24:
        return 
    global cnt
    for i in range(len(lst)):
        if lst[i][0] >= time:
            cnt += 1
            truck(lst[i+1:], lst[i][1])
            break

T = int(input())
for t in range(1, T+1):
    n = int(input())
    task = []
    for _ in range(n):
        s, e = map(int, input().split())
        task.append((s, e))

    task.sort(key = lambda x: x[1])
    cnt = 0
    truck(task, 0)
    print(f'#{t}', cnt)