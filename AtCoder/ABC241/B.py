from collections import Counter


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def main():
    cnts = Counter(A)
    for val in B:
        if val not in cnts:
            return False
        
        if cnts[val] == 0:
            return False
        else:
            cnts[val] -= 1

    return True

print("Yes" if main() else "No")