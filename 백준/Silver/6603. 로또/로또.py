def combination(num, s):
    for n1 in range(num):
        for n2 in range(n1+1, num):
            for n3 in range(n2+1, num):
                for n4 in range(n3+1, num):
                    for n5 in range(n4+1, num):
                        for n6 in range(n5+1, num): 
                            print(s[n1], s[n2], s[n3], s[n4], s[n5], s[n6])

while True:
    n = list(map(int, input().split()))
    if len(n) == 1:
        break
    k = n[0]
    combination(k, n[1:])
    print()