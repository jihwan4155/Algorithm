def post_order(v):
    if tree[v] == 0: 
        post_order(v*2) # 왼쪽 자식 노드 계속 들어가기
    if v * 2 + 1 < n + 1:
        post_order(v*2+1) # 오른쪽 자식 노드 계속 들어가기
    if v // 2 > 0: # 재귀 안들어가면 부모 노드에 더하기 (부모노드 인덱스 = 자식노드 인덱스 // 2 )
        tree[v//2] += tree[v]


T = int(input())
for t in range(1, T+1):
    n, m, l = map(int, input().split())

    tree = [0] * (n+1)
    for i in range(m):  # 리프 노드들의 value 값 저장
        idx, value = map(int, input().split())
        tree[idx] = value

    post_order(1)
    print(f'#{t}', tree[l])