class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = 0
        if low % 2 != 0:
            ans += 1
            low += 1
        if high % 2 != 0:
            ans += 1
            high -= 1
        return ans + (high - low) // 2

low = 3
high = 7
print(Solution().countOdds(low, high))