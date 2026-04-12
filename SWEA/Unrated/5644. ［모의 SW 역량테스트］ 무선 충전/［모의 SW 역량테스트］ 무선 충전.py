from collections import defaultdict

def check_if_in(idx):
    # bc 범위 안인지 체크
    in_bc = []
    for k, v in bc.items():
        if v[2] >= abs(idx[0] - v[0]) + abs(idx[1] - v[1]):
            in_bc.append(k)
    return in_bc


T = int(input())
for tc in range(1, T+1):
    m, a = map(int, input().split()) # 이동 시간, BC개수
    route_a = [0] + list(map(int, input().split()))
    route_b = [0] + list(map(int, input().split()))
    # 0 이동x, 1 하, 2 우, 3 상, 4 좌
    move = {0: (0, 0), 1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}

    bc = defaultdict(list)
    for i in range(1, a+1):
        bc[i] = list(map(int, input().split()))
        # i: x, y, 거리, power

    ans = 0
    a_idx = [1, 1] # 출발 위치
    b_idx = [10, 10]
    time = 0

    while time <= m:
        a_idx[0] = a_idx[0] + move[route_a[time]][0]
        a_idx[1] = a_idx[1] + move[route_a[time]][1]
        b_idx[0] = b_idx[0] + move[route_b[time]][0]
        b_idx[1] = b_idx[1] + move[route_b[time]][1]

        a_bc, b_bc = check_if_in(a_idx), check_if_in(b_idx)

        if a_bc and b_bc:
            max_check = 0
            for i in a_bc:
                for j in b_bc:
                    check = 0
                    if i == j:
                        check = bc[i][3]
                    else:
                        check = bc[i][3] + bc[j][3]
                    max_check = max(max_check, check)
            ans += max_check

        elif a_bc:
            a_check = 0
            for i in a_bc:
                a_check = max(a_check, bc[i][3])
            ans += a_check

        elif b_bc:
            b_check = 0
            for i in b_bc:
                b_check = max(b_check, bc[i][3])
            ans += b_check

        time += 1
    
    print(f'#{tc}', ans)