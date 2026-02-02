import sys

N = int(sys.stdin.readline()) # 색종이 개수
field = [[0] * 1001 for _ in range(1001)] # 1001 * 1001 평면

# 자리를 하나하나 다 재할당 후 순회하며 개수 세기
for num in range(1, N+1): # 색종이 번호 순회
    X, Y, width, height = map(int, sys.stdin.readline().split())
    for y in range(Y, Y + height):
        field[y][X:(X + width)] = [num] * width
        # 해당 위치부터 끝 위치까지 슬라이싱으로 모두 색종이 번호 할당
        # field[y][x]형식으로 for 문 3개 쓰면 부분 정답

for num in range(1, N+1):
    seen = 0
    for row in field: # 평면 순회하면서 번호별 색종이 개수 합 구하기
        seen += row.count(num)
    print(seen)