def main():
    S = input()
    
    if len(S) != 8:
        return False
    
    return S[0].isupper() and S[-1].isupper() and S[1:7].isnumeric() and int(S[1:7]) >= 100000 and int(S[1:7]) <= 999999


if __name__ == "__main__":
    print("Yes" if main() else "No")