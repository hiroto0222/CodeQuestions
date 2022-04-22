# class Solution(object):
#     def numSubarrayBoundedMax(self, nums, left, right):
#         """
#         :type nums: List[int]
#         :type left: int
#         :type right: int
#         :rtype: int
#         """
#         curr_max = 0
#         n = len(nums)
#         i = 0
#         curr_dp = []
#         ans = 0
#         while i < n:
#             curr_max = nums[i]
#             if nums[i] >= left and nums[i] <= right:
#                 curr_dp.append(1)

#                 for j in range(i + 1, n):
#                     curr_max = max(curr_max, nums[j])
#                     if curr_max < left or curr_max > right:
#                         i = j + 1
#                         break

#                     if nums[j] >= left and nums[j] <= right:
#                         curr_dp.append(1)
#                     else:
#                         curr_dp.append(0)

#                 else:
#                     i = n

#                 prev = 1
#                 curr_ans = sum(range(1, len(curr_dp) + 1))
#                 curr_cnt = 0
#                 x = 0
#                 for l in range(len(curr_dp) - 1, -1, -1):
#                     if curr_dp[l] == 0:
#                         if prev == 0:
#                             x += 1
#                         curr_cnt += (1 + x)
#                         prev = 0
#                     else:
#                         prev = 1
#                         x = 0
#                 curr_ans = curr_ans - curr_cnt
#                 # print(curr_dp, curr_ans)
#                 ans += curr_ans
#                 curr_dp = []

#             else:
#                 if curr_max < left:
#                     curr_dp.append(0)
#                 elif curr_max > right:
#                     curr_dp = []
#                 i += 1

#         return ans

# class Solution(object):
#     def getNumberSubArraysInRange(self, nums, left, right):
#         """
#         :type nums: List[int]
#         :type left: int
#         :type right: int
#         :rtype: int
#         """
#         n = len(nums)
#         cnt = left_p = right_p = 0

#         while left_p < n and right_p < n:
#             if nums[left_p] > right:
#                 left_p += 1
#             else:
#                 right_p = left_p
#                 while right_p < n and left <= nums[right_p] <= right:
#                     right_p += 1
    
#                 sub_arr_size = right_p - left_p
#                 sub_arr_cnt = (sub_arr_size * (sub_arr_size + 1)) // 2
#                 cnt += sub_arr_cnt
#                 left_p = right_p
        
#         return cnt
    

#     def getSubArrayCount(self, nums, left, right):
#         n = len(nums)
#         if not n:
#             return 0
        
#         count_less_left = Solution().getNumberSubArraysInRange(nums, float('-inf'), left-1)
#         count_less_right = Solution().getNumberSubArraysInRange(nums, float('-inf'), right)
#         return count_less_right - count_less_left


# nums = [876,880,482,260,132,421,732,703,795,420,871,445,400,291,358,589,617,202,755,810,227,813,549,791,418,528,835,401,526,584,873,662,13,314,988,101,299,816,833,224,160,852,179,769,646,558,661,808,651,982,878,918,406,551,467,87,139,387,16,531,307,389,939,551,613,36,528,460,404,314,66,111,458,531,944,461,951,419,82,896,467,353,704,905,705,760,61,422,395,298,127,516,153,299,801,341,668,598,98,241]
# left = 658
# right = 719

# print(Solution().getSubArrayCount(nums, left, right))


# O(n) time and O(1) space
# class Solution(object):
#     def getSubArrayCount(self, nums, left, right):
#         i, j = 0, 0
#         n = len(nums)
#         cnt = 0
#         ans = 0

#         while i <= j and j < n:
#             if left <= nums[j] <= right:
#                 cnt = (j - i + 1)
#                 ans += (j - i + 1)

#             elif right < nums[j]:
#                 i = j + 1
#                 cnt = 0
            
#             else:
#                 ans += cnt
            
#             j += 1

#         return ans

# # nums = [7, 3, 6, 7, 1]
# # left = 1
# # right = 4

class Solution(object):
    def getSubArrayCount(self, nums, left, right):
        i, j = 0, 0
        n = len(nums)
        cnt = 0
        ans = 0
        
        while i <= j and j < n:
            if left <= nums[j] <= right:
                cnt = (j - i + 1)
                ans += (j - i + 1)
            
            elif nums[j] > right:
                cnt = 0
                i = j + 1
            
            else:
                ans += cnt
            
            j += 1

        return ans

nums = [7, 3, 6, 7, 1]
left = 1
right = 4

nums = [2,9,2,5,6]
left = 2
right = 8

# nums = [876,880,482,260,132,421,732,703,795,420,871,445,400,291,358,589,617,202,755,810,227,813,549,791,418,528,835,401,526,584,873,662,13,314,988,101,299,816,833,224,160,852,179,769,646,558,661,808,651,982,878,918,406,551,467,87,139,387,16,531,307,389,939,551,613,36,528,460,404,314,66,111,458,531,944,461,951,419,82,896,467,353,704,905,705,760,61,422,395,298,127,516,153,299,801,341,668,598,98,241]
# left = 658
# right = 719

print(Solution().getSubArrayCount(nums, left, right))
