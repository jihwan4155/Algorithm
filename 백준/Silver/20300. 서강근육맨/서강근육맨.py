def check_minimum(mac_lst):
    sorted_lst = sorted(mac_lst) # 오름차순으로 정리

    max_num = sorted_lst[-1] + sorted_lst[0] # 가장 작은 수와 큰 수를 최대값으로 설정

    if len(mac_lst) % 2 != 0: # 갯수가 홀수이면
        max_num = sorted_lst[-1]    # 제일 큰 수로 최대값 초기화 후 pop
        sorted_lst.pop()

    while sorted_lst: 
        if sorted_lst[-1] + sorted_lst[0] > max_num: # 최대값 보다 클 시 
            max_num = sorted_lst[-1] + sorted_lst[0] #  최대값 초기화
        
        sorted_lst.pop(0) # 검사한 앞 뒤 pop
        sorted_lst.pop(-1) 

    return max_num

N = int(input())
machines = list(map(int, input().split()))

print(check_minimum(machines))
