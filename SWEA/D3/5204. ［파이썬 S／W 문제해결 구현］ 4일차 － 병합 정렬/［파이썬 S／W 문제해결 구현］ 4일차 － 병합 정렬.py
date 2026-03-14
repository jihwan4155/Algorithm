def merge(left, right):
    global cnt

    result = [0] * (len(left) + len(right))
    l = r = 0
    if left[-1] > right[-1]:
        cnt += 1

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1
    
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result 


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    
    mid = len(lst) // 2

    left = lst[:mid]
    right = lst[mid:]

    left_lst = merge_sort(left)
    right_lst = merge_sort(right)

    merge_lst = merge(left_lst, right_lst)
    return merge_lst

T = int(input())
for t in range(1, T+1):
    n = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    sorted_num = merge_sort(num)
    print(f'#{t} {sorted_num[n//2]} {cnt}')