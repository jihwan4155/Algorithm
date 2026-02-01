N = int(input()) # 색종이 개수
field = [[0] * 1001 for _ in range(1001)] # 1001 * 1001 평면

for num in range(1, N+1): # 색종이 번호 순회
    X, Y, width, height = map(int,input().split())
    for y in range(Y, Y + height):
        for x in range(X, X + width):
            field[y][x] = num # 해당 위치 모두 색종이 번호 할당

for num in range(1, N+1):
    seen = 0 
    for u in field: # 평면 순회하면서 번호별 색종이 개수 합 구하기
        seen += u.count(num) 
    print(seen)