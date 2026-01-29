def check_minimum(mac_lst):
    sorted_lst = sorted(mac_lst)

    max_num = sorted_lst[-1] + sorted_lst[0]

    if len(mac_lst) % 2 != 0:
        max_num = sorted_lst[-1]
        sorted_lst.pop()

    while sorted_lst:
        if sorted_lst[-1] + sorted_lst[0] > max_num:
            max_num = sorted_lst[-1] + sorted_lst[0]
        
        sorted_lst.pop(0)
        sorted_lst.pop(-1)

    return max_num

N = int(input())
machines = list(map(int, input().split()))

print(check_minimum(machines))