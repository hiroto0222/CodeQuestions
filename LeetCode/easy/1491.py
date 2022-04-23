from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal, max_sal = min(salary), max(salary)
        return (sum(salary) - (min_sal + max_sal)) / (len(salary) - 2)
        

salary = [1000,2000,3000]
print(Solution().average(salary))