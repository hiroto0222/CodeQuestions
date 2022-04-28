from functools import reduce
from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(product):
            if product > 0: return 1
            if product < 0: return -1
            else: return 0
            
        product = reduce(lambda x, y: x * y, nums)
        return signFunc(product)