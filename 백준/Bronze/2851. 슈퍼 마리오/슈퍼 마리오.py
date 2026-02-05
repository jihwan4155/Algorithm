mush = [int(input()) for _ in range(10)]

score = 0 # 누적 점수
check = []
for i in range(10):
    score += mush[i]
    if score > 100: # 100 넘어가는 순간 
        check.append(score - mush[i]) # 넘어가기 전 총 점수 
        check.append(score) # 넘어간 후 총 점수 
        break
    elif score == 100: # 딱 100이면 100 출력
        print(score)
        break
else:
    print(score) # 10개까지 합했는데도 100이 안됐을때... 이 반례를 까먹음..

if len(check) > 0: # check가 비어있으면 100이 었다는것.
    if 100 - check[0] < check[1] - 100: # 100 넘어가기 전 수가 100이랑 더 가까우면
        print(check[0])
    elif 100 - check[0] > check[1] - 100: # 100 넘어간 후 수가 100이랑 더 가까우면
        print(check[1])
    else: # 넘어가기전 넘어간후 수가 같으면 넘어간 후 수 print
        print(check[1])