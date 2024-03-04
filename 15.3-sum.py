#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n-2):
            l = i + 1
            r = n - 1
            while (l < r):
                total = nums[i] + nums[l] +nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.add((nums[i] , nums[l] ,nums[r]))
                    l += 1
        return res
# @lc code=end

