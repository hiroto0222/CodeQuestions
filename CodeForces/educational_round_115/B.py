"""
n students is even
divided into 2 groups with same number of students

brute force -> check all pair of days
keep count of:
    only day A => cnt_a 
    only day B => cnt_b
if cnt_a > n // 2 or cnt_b > n // 2 -> then NO
else -> YES
"""

for _ in range(int(input())):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    ans = "NO"

    for day_a in range(5):
        for day_b in range(day_a + 1, 5):
            cnt_a, cnt_b, cnt_no = 0, 0, 0
            for i in range(n):
                if (grid[i][day_a] == 1):
                    cnt_a += 1
                if (grid[i][day_b] == 1):
                    cnt_b += 1
                if (grid[i][day_a] == 0 and grid[i][day_b] == 0):
                    cnt_no += 1
            if (cnt_a >= n // 2 and cnt_b >= n // 2 and cnt_no == 0):
                ans = "YES"
                break
    
    print(ans)