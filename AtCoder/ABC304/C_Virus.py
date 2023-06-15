N, D = map(int, input().split())
coords = list(tuple(map(int, input().split())) for _ in range(N))


def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


stack = [coords[0]]
virus = set([0])

while stack:
    curr = stack.pop()
    for i, coord in enumerate(coords):
        if i not in virus and dist(curr, coord) <= D:
            stack.append(coord)
            virus.add(i)

for i in range(N):
    if i in virus:
        print("Yes")
    else:
        print("No")
