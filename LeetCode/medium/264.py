class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        index2, index3, index5 = 0, 0, 0
        factor2, factor3, factor5 = 2, 3, 5
        for i in range(1, n):
            min_ = min([factor2, factor3, factor5])
            print(factor2, factor3, factor5, min_)
            ugly[i] = min_
            print(ugly)
            if factor2 == min_:
                index2 += 1
                factor2 = 2*ugly[index2]
            if factor3 == min_:
                index3 += 1
                factor3 = 3*ugly[index3]
            if factor5 == min_:
                index5 += 1
                factor5 = 5*ugly[index5]
        
        return ugly[-1]


n = 10
print(Solution().nthUglyNumber(n))