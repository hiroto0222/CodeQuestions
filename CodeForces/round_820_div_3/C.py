from collections import defaultdict

for _ in range(int(input())):
    # get to nth tile with min cost but max jumps
    # ord(char) - 96 is index of char
    # cost = abs(ord(s[i]) - ord(s[j]))
    # min cost is always ord(s[n - 1]) - ord([s[0]])
    # keep track of indexes of each letter
    
    s = input()
    n = len(s)

    start = ord(s[0])
    end = ord(s[n - 1])
    cost = abs(start - end)
    m = 0

    indexes = defaultdict(list)
    for i, char in enumerate(s):
        if (i == 0): continue

        val = ord(char)
        if val in indexes:
            indexes[val].append(i + 1)
        else:
            indexes[val] = [i + 1]

    ans = [1]
    inc = 1 if end >= start else -1
    for val in range(start, end + inc, inc):
        if val in indexes:
            ans.extend(indexes[val])
            
    print(cost, len(ans))
    print(*ans)