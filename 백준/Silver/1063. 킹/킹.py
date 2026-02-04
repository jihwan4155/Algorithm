king_0, stone, N = map(str, input().split()) # 킹, 돌의 첫 좌표, 명령 수

call = [] # 명령 집합
for _ in range(int(N)):
    c = input()
    call.append(c)

row = [chr(i) for i in range(ord('A'), ord('H') + 1)]
        # A ~ H 까지 row [A, B, C, ---, G, H]

def go_move(x, y, cmd):

    move = {
        'R':(1, 0), 'L':(-1, 0), 'B':(0, -1), 'T':(0, 1), 
        'RT':(1, 1), 'LT':(-1, 1), 'RB':(1, -1), 'LB':(-1, -1),
        } # 명령별 이동 인덱스

    xx = x + move[cmd][0] # 명령으로 바뀐 x 인덱스
    yy = y + move[cmd][1] # 명령으로 바뀐 y 인덱스

    if xx < 0 or xx > 7 or yy < 0 or yy > 7: # 체스판 밖으로 가는 범위인지 체크
        return x, y # 체스판 밖으로 가는 범위라면 그대로 return
    
    return xx, yy # 체스판 안이면 이동 후 인덱스 return

king_x = row.index(king_0[0]) # 킹의 처음 row 위치
king_y = int(king_0[1]) - 1 # 킹의 처음 column 위치
dol_x = row.index(stone[0]) # 돌의 처음 row 위치
dol_y = int(stone[1]) - 1 # 돌의 처음 column 위치

for cmd_ in call:
    move_x, move_y = go_move(king_x, king_y, cmd_) # 킹 이동
    move_dox, move_doy = dol_x, dol_y # 돌이 원래 있던 위치 변수 할당
    if move_x == dol_x and move_y == dol_y: # 가려는 자리에 돌이 있다면 
        move_dox, move_doy = go_move(dol_x, dol_y, cmd_) # 돌 이동 확인
        if move_dox == dol_x and move_doy == dol_y: # 돌 이동 함수 값이 그대로 나왔으면 
            
            continue # 돌이 체스판 넘어가는 범위였기에 무효 and 다음 명령
            
    king_x, king_y, dol_x, dol_y = move_x, move_y, move_dox, move_doy
    # 킹 x, y + 돌 x, y 인덱스 명령 끝날때마다 초기화

print(row[king_x] + str(king_y + 1)) # 인덱스로 접근했기 때문에
print(row[dol_x] + str(dol_y + 1)) # y + 1? 문제에는 체스판의 column이 0이 아닌 1부터 시작
                                    # x 인덱스로 알파벳으로 변환, y 값은 + 1