"""
make min of a to be maximal
if no negative numbers exist -> 0 operations
sort a -> O(n log n)
iterate through a until 1 element -> O(n)
"""


from math import inf

def main():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(a[0])
        return
    
    a.sort(reverse=True)
    to_minus = 0
    curr_max = a[-1]

    while a:
        curr = a.pop() - to_minus
        if a:
            curr_max = max(curr_max, a[-1] - to_minus - curr)
            to_minus += curr
        else:
            curr_max = max(curr_max, curr)
            break
    
    print(curr_max)


for _ in range(int(input())):
    main()