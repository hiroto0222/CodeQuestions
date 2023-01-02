# letters A, B, C
# - erase 1 A and 1 B
# - erase 1 B and 1 C
# sequence to empty string
# ABACAB -> 

def main():
    s = input()
    a_cnt = s.count('A')
    b_cnt = s.count('B')
    c_cnt = s.count('C')

    if (a_cnt + c_cnt == b_cnt):
        return True
    return False


for _ in range(int(input())):
    print("Yes" if main() else "No")
