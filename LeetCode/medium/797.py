from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # dfs
        self.ans = []
        n = len(graph)

        def dfs(node, path):
            print(path)
            if node == n - 1:
                self.ans.append(path)
            for nextNode in graph[node]:
                dfs(nextNode, path + [nextNode])
        
        dfs(0, [0])
        return self.ans


graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(Solution().allPathsSourceTarget(graph))