from typing import List
from heapq import heapify, heappop, heappush, nlargest
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = Counter(nums)
        pq = []
        for key in cnts.keys():
            heappush(pq, (cnts[key], key))
        
        return [nlargest(k, pq)[i][1] for i in range(k)]

print(Solution().topKFrequent([1,1,1,2,2,3], 2))