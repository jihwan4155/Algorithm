field_w, field_h = map(int, input().split())
n = int(input())

width = [0] # 가장 앞의 수를 0
height = [0]
width.append(field_w) # 끝 번호 추가
height.append(field_h)

for _ in range(n):
    line, h = map(int, input().split())
    if line == 1:
        width.append(h) # 세로선이면 가로 리스트에 더하기
    else:
        height.append(h) # 가로선이면 세로 리스트에 더하기

srt_wid = sorted(width) # 순서로 정렬
srt_hgt = sorted(height) 

m_wth = 0 
m_hgt = 0

for i in range(1, len(srt_wid)): # 가로
    max_w = srt_wid[i] - srt_wid[i-1] # 지금 번호에서 전의 번호까지 거리
    if max_w > m_wth: # 더 크면 초기화
        m_wth = max_w

for j in range(1, len(srt_hgt)): # 세로
    max_h = srt_hgt[j] - srt_hgt[j-1] 
    if max_h > m_hgt:
        m_hgt = max_h

print(m_wth * m_hgt) # 넓이 구하기