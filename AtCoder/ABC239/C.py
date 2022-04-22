def f(xa, ya, xb, yb):
    return (xa - xb)**2 + (ya - yb)**2


def main():
    x1, y1, x2, y2 = map(int, input().split())
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            xt = x1 + dx
            yt = y1 + dy
            if f(xt, yt, x1, y1) == 5 and f(xt, yt, x2, y2) == 5:
                return True
    
    return False

print("Yes" if main() else "No")