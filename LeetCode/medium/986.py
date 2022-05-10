from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            s1, e1 = firstList[i][0], firstList[i][1]
            s2, e2 = secondList[j][0], secondList[j][1]
            if e2 >= s1 and s2 <= e1:
                # intersection found
                ans.append([max(s1, s2), min(e1, e2)])
            
            if e2 > e1:
                i += 1
            else:
                j += 1
        
        return ans


firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
print(Solution().intervalIntersection(firstList, secondList))