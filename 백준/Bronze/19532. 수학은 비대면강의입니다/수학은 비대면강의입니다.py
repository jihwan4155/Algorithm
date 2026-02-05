a, b, c, d, e, f = map(int, input().split())

if (a*e - d*b) != 0: # 분모가 0이 안닐때
    x = (c*e - b*f)//(a*e - d*b) # 0이면 문제가 성립이 안됨
    
if b != 0: # 분모가 0이 아닐때
    y = (c - x * a)//b
else:
    y = (f - d * x)//e

print(x, y)