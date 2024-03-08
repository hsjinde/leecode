#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         return nums[i+1]
        # return nums[0]
        
        # nums.sort()
        # return nums[0]

        ans = nums[0]
        low,high = 0, len(nums) - 1
        if nums[low] < nums[high]:
            return nums[low]
        while(low <= high):
            if nums[low] < nums[high]:
                ans = min(ans, nums[low])
                break
            mid = (low + high) // 2 
            ans = min(ans, nums[mid])
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid -1
        return ans
# @lc code=end


#Time complexity: O(logn) 
#T(n) = O(1) + O(n/2)
#Space complexity: 
