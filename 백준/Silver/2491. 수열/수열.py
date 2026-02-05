N = int(input())
nums = list(map(int, input().split()))

incre_length = decre_length = 1 # 증가수열, 감소수열 
longest = 1 # 최장 수열

for i in range(1, N): # 처음꺼와 마지막 인덱스 제외
    if nums[i] >= nums[i-1]: # 전의 수보다 크거나 같으면
        incre_length += 1 # 증가 수열 + 1
    else:
        incre_length = 1 # 작다면 다시 1로 초기화
    
    if nums[i] <= nums[i-1]: # 전의 수보다 작거나 같으면
        decre_length += 1 # 감소수열 + 1
    else:
        decre_length = 1 # 크다면 다시 1로 초기화
    
    longest = max(longest, incre_length, decre_length)
    # 최장수열, 증가 수열, 감소수열 중의 최대값으로 초기화
print(longest)