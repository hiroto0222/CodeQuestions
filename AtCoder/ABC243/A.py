# F, M, T
V, A, B, C = map(int, input().split())
while V >= 0:
    V -= A
    if V < 0:
        print('F')
        exit()
    V -= B
    if V < 0:
        print('M')
        exit()
    V -= C
    if V < 0:
        print('T')
        exit()    