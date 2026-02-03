# 리스트 슬라이싱 풀이
# T = int(input())

# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
    
#     for b in range(len(B)):
#         for a in range(len(A)):
#             if B[b] == A[a]:
#                 B[b] = 0
#                 A[:a + 1] = [0] * a
#                 break
    
#     for i in B:
#         if i != 0:
#             print(f'#{t} NO')
#             break
#     else:
#         print(f'#{t} YES')

# 투 포인터 풀이 (정석)
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    start_a = 0 # 리스트 A 시작 포인터
    end_b = 0 # 리스트 B 시작 포인터
    cnt = 0 # 같은 수 있으면 + 1
    while end_b < M:
        if A[start_a] == B[end_b]: # 값이 같다면
            cnt += 1 
            end_b += 1 # B 시작 포인터 다음 포인터로 
        
        start_a += 1 # A 시작 포인터 루프마다 항상 + 1

        if start_a == N: # A 최대 인덱수 넘으면 break
            break

    if cnt == M:
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')