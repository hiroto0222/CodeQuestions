"""
all elements in array are the same
ex: [3, 4, 2, 4, 1, 2] -> [4, 4, 4, 4, 4, 4]
max element - min element
"""

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a) - min(a))

