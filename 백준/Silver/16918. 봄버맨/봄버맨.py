r, c, n = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(r)]
full = [['O']*c for _ in range(r)]

if n%2 == 0:
    for b in range(r):
        print(''.join(full[b]))
elif n == 1:
    for b in range(r):
        print(''.join(arr[b]))
elif n%4 == 3:
    for j in range(r):
        for i in range(c):
            if arr[j][i] == 'O':
                full[j][i] = '.'
                for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    jy = j + dy
                    ix = i + dx
                    if 0 <= jy < r and 0 <= ix < c:
                        full[jy][ix] = '.'
    for s in range(r):
        print(''.join(full[s]))
else:
    for j in range(r):
        for i in range(c):
            if arr[j][i] == 'O':
                full[j][i] = '.'
                for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    jy = j + dy
                    ix = i + dx
                    if 0 <= jy < r and 0 <= ix < c:
                        full[jy][ix] = '.'
    arr = [['O']*c for _ in range(r)]
    for j in range(r):
        for i in range(c):
            if full[j][i] == 'O':
                arr[j][i] = '.'
                for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    jy = j + dy
                    ix = i + dx
                    if 0 <= jy < r and 0 <= ix < c:
                        arr[jy][ix] = '.'
    for p in range(r):
        print(''.join(arr[p]))