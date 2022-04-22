"""
[#, #]
[#, #]
can go diagonal or adjacent by 1

keep stack of visited -> pop from stack
keep set of seen

do till popped item = (1, n - 1) -> "YES"
or till stack is empty -> "NO"
"""

for _ in range(int(input())):
    n = int(input())
    grid = [list(map(int, list(input()))) for _ in range(2)]

    stack = [(0, 0)]
    seen = set()
    ans = "NO"
    while stack:
        i, j = stack.pop()

        if (i, j) == (1, n - 1):
            ans = "YES"
            break
        
        # check for top row
        if (i == 0):
            # add bot
            if ((i + 1, j) not in seen and grid[i + 1][j] != 1):
                stack.append((i + 1, j))
            # check left
            if (j > 0):
                if (((i, j - 1) not in seen) and grid[i][j - 1] != 1):
                    stack.append((i, j - 1))
                if (((i + 1, j - 1) not in seen) and grid[i + 1][j - 1] != 1):
                    stack.append((i + 1, j - 1))
            # check right
            if (j < n - 1):
                if (((i, j + 1) not in seen) and grid[i][j + 1] != 1):
                    stack.append((i, j + 1))
                if (((i + 1, j + 1) not in seen) and grid[i + 1][j + 1] != 1):
                    stack.append((i + 1, j + 1))

        else:
            # add top
            if ((i - 1, j) not in seen and grid[i - 1][j] != 1):
                stack.append((i - 1, j))
            # check left
            if (j > 0):
                if (((i, j - 1) not in seen) and grid[i][j - 1] != 1):
                    stack.append((i, j - 1))
                if (((i - 1, j - 1) not in seen) and grid[i - 1][j - 1] != 1):
                    stack.append((i - 1, j - 1))
            # check right
            if (j < n - 1):
                if (((i, j + 1) not in seen) and grid[i][j + 1] != 1):
                    stack.append((i, j + 1))
                if (((i - 1, j + 1) not in seen) and grid[i - 1][j + 1] != 1):
                    stack.append((i - 1, j + 1))
        
        seen.add((i, j))

    print(ans)