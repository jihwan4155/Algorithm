def find_page(total, ret): # 이진탐색 횟수 계산 함수
    l = 1 # 초기 1페이지
    r = total # 오른쪽 초기 책 최대 페이지 수
    times = 0 # 이진탐색한 수
    while True:
        if total != ret: # 타겟팅 페이지가 아니라면
            total = (l + r)//2 # 이진탐색
            if total < ret: # 결과가 타겟팅 보다 작다면
                l = total # 왼쪽 구간 초기화
            elif total > ret: # 반대라면
                r = total # 오른쪽 구간 초기화
            else: # 같다면
                times += 1 
                return times # 리턴
        else:
            break

        times += 1

    return times   

T = int(input())

for t in range(1, T+1):
    pages, A, B = map(int, input().split())
    A_num = find_page(pages, A) # 총페이지, A 타겟
    B_num = find_page(pages, B) 
    if A_num < B_num:
        print(f'#{t} A')
    elif B_num < A_num:
        print(f'#{t} B')
    else:
        print(f'#{t}', 0)