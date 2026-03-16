import sys
sys.setrecursionlimit(10**6)

def recur(x):
    if x <= 1:
        return 1
    else:
        return x * recur(x-1)

n = int(input())

print(recur(n))