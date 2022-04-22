S = input()
T = input()

def main():
    if S == T:
        return True

    for i in range(len(S) - 1):
        curr = S[:i] + S[i + 1] + S[i] + S[i + 2:]
        if curr == T:
            return True
    
    return False

print("Yes" if main() else "No")