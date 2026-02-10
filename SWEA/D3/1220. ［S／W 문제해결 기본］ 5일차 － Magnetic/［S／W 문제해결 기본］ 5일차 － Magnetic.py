for t in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    deadlock = 0
    for i in range(100): # 열
        stack = []
        for j in range(100): # 행
            mgn = arr[j][i]
            if mgn != 0: # 0은 무시 0 이 아닌건 stack 추가
                stack.append(mgn)
        if len(stack) < 2: # 비거나 하나 있으면 패스
            continue
        
        # 밖으로 나가는 자석들 제거
        while len(stack) > 0 or stack[0] == 2 or stack[-1] == 1:
            if stack[0] == 2:
                stack.pop(0)
            if stack[-1] == 1:
                stack.pop()
            if len(stack) < 2 or (stack[0] != 2 and stack[-1] != 1):
                break
        
        # 다 나가거나 하나 남으면 패스
        if len(stack) < 2:
            continue

        last = stack[0] # 1 2 1 2 형식으로 교착된 자석 + 1
        check = 1
        idx = 1
        while idx < len(stack):
            if stack[idx] != last:
                last = stack[idx]
                check += 1
            idx += 1

        deadlock += check//2 # 교착된 한 쌍의 자석들 총 수 // 2
    print(f'#{t}', deadlock)