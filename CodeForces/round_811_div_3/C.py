def main():
    # min val with distinct digits
    # start from first digit 9 and keep going

    curr_sum = int(input())
    i = 0
    curr_val = 9
    ans = 0

    while curr_sum > 0:
        if (curr_sum >= curr_val):
            ans += curr_val * 10**i
        else:
            ans += curr_sum * 10**i
        
        curr_sum -= curr_val
        i += 1
        curr_val -= 1

    return ans


for _ in range(int(input())):
    print(main())