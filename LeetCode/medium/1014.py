from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # greedily take largest values -> currLargest
        # if values[i] + currLargest - i > res -> update res
        # if values[i] + i > currLargest -> update currLargest
        # O(N) time, O(1) space
        
        currLargest = res = 0
        for i in range(len(values)):
            if values[i] + currLargest - i > res:
                res = values[i] + currLargest - i
            
            if values[i] + i > currLargest:
                currLargest = values[i] + i
            
        return res


values = [8,1,5,2,6]
print(Solution().maxScoreSightseeingPair(values))