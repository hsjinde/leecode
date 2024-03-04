#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for num in nums:
            curSum += num
            maxSum = max(curSum, maxSum)
            curSum = max(0, curSum)
        return maxSum
        
# @lc code=end

