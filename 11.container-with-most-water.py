#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1
        while(l < r):
            water = min(height[l], height[r])*(r - l)
            max_area = max(water, max_area)
            if height[l] > height[r]:        
                r -= 1
            else:
                l += 1
        return max_area 
# @lc code=end

#Time complexity: O(n)
#Space complexity: O(1)