"""
Find the Kth lowest price for buying tako where
1. need to buy atleast 1
2. allowed to buy multiple of the same

only need K elements in heap
"""
from heapq import heappush

N, K = map(int, input().split())
A = list(map(int, input().split()))

if K == 1:
    print(min(A[0]))

heap = []
