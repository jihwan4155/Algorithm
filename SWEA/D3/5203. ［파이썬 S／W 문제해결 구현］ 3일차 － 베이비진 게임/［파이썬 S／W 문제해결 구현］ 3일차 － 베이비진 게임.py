def baby(player):
    sset = set(player)
    s_player = sorted(sset)
    for j in sset:
        if player.count(j) >= 3:
            return 1
    if len(player) >= 3:
        for i in range(len(s_player)-2):
            if s_player[i]+1 == s_player[i+1] and s_player[i+1]+1 == s_player[i+2]:
                return 1
    return 0

T = int(input())
for t in range(1, T+1):
    card = list(map(int, input().split()))
    p1 = [card[0]]
    p2 = []
    for i in range(1, 12):
        if i % 2 == 0:
            p1.append(card[i])
            if baby(p1) == 1:
                print(f'#{t}', 1)
                break
        else:
            p2.append(card[i])
            if baby(p2) == 1:
                print(f'#{t}', 2)
                break
    else:
        print(f'#{t}', 0)
            