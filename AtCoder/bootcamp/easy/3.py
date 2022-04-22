"""
s[i] = a -> kokunai
s[i] = b -> kaigai
s[i] = c -> else
"""

N, A, B = map(int, input().split())
S = input()

curr_a, curr_b, curr_b_rank = 0, 0, 1
for i in range(N):
    if S[i] == "a":
        if (curr_a + curr_b) < (A + B):
            print("Yes")
            curr_a += 1
        else:
            print("No")
    elif S[i] == "b":
        if (curr_a + curr_b) < (A + B) and curr_b_rank <= B:
            print("Yes")
            curr_b += 1
            curr_b_rank += 1
        else:
            print("No")
    else:
        print("No")