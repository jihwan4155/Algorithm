mapping = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

def code(letter):
    check = ''
    for i in range(0, 56, 7):
        check += str(mapping[letter[i:i+7]])
    
    even = 0
    odd = 0
    for i in range(len(check)):
        if (i+1)%2 == 1:
            odd += int(check[i])
        else:
            even += int(check[i])
    
    ans = odd*3 + even
    if ans%10 == 0:
        return odd+even
    else:
        return 0


T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = set()
    for _ in range(n):
        a = input()
        arr.add(a) # 중복 제거로 받기

    flag = False

    for i in arr:
        for idx in range(m-1, -1, -1):
            if i[idx] == '1':
                solve = code(i[idx-55:idx+1])
                print(f'#{t}', solve)
                flag = True
                break
            if idx < 55:
                break
        if flag:
            break