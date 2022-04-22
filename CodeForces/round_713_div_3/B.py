t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append([i for i in input()])

    pos = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '*':
                pos.append([i, j])

    arr[pos[0][0]][pos[1][1]] = '*'
    arr[pos[0][1]][pos[1][0]] = '*'

    for i in range(n):
        print(''.join(arr[i]))
    