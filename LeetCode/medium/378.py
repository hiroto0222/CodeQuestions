from heapq import heappush, heappop, heapify

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        r, c = len(matrix), len(matrix[0])
        seen = set()  # keep track of (i, j)
        heap = []
        heappush(heap, (matrix[0][0], 0, 0))  # push (val, i, j)
        seen.add((0, 0))

        while (k > 1):
            _, i, j = heappop(heap)
            if (j + 1) < r and (i, j + 1) not in seen:
                heappush(heap, (matrix[i][j + 1], i, j + 1))
                seen.add((i, j + 1))
            if (i + 1) < c and (i + 1, j) not in seen:
                heappush(heap, (matrix[i + 1][j], i + 1, j))
                seen.add((i + 1, j))
            k -= 1

        return heappop(heap)[0]

print(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
print(Solution().kthSmallest(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], k = 3))
print(Solution().kthSmallest(matrix = [[1,2],[1,3]], k = 2))