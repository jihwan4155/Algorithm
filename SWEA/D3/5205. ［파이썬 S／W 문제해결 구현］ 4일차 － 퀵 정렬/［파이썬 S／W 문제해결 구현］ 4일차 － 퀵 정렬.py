def quick_sort(start, end):
    if start >= end:
        return
    
    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    quick_sort(start, right-1)
    quick_sort(right+1, end)


T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, n-1)
    print(f'#{t}', arr[n//2])