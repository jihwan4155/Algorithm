n = int(input())

def pre_order(v):
    if v:
        print(v, end='')
        pre_order(left[v])
        pre_order(right[v])

def in_order(v):
    if v:
        in_order(left[v])
        print(v, end='')
        in_order(right[v])

def post_order(v):
    if v:
        post_order(left[v])
        post_order(right[v])
        print(v, end='')


left = {chr(65+i) : '' for i in range(n)}
right = {chr(65+i) : '' for i in range(n)}
par = {chr(65+i) : '' for i in range(n)}

for i in range(n):
    node, lc, rc = map(str, input().split())
    if rc != '.':
        right[node] = rc
    if lc != '.':
        left[node] = lc

pre_order('A')
print()
in_order('A')
print()
post_order('A')

