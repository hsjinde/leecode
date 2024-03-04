#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        l1 = [1] * length
        l2 = [1] * length
        res = [1] * length
        for i in range(1, length):
            l1[i] = nums[i-1] * l1[i -1]
        for i in range(length-2, -1, -1):
            l2[i] = nums[i+1] * l2[i+1]
        for i in range(length):
            res[i] = l1[i] * l2[i]
        return res
# @lc code=end

