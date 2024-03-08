class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        for i in nums:
            if i == 0:
                curMin, curMax = 1, 1
            tmpMax = i * curMax
            tmpMin = i * curMin
            curMax = max(tmpMax, tmpMin, i)
            curMin = min(tmpMax, tmpMin, i)
            res = max(res, curMax)
        return res
        
#Time complexity: O(n)
#where n is the length of the input array nums. We iterate through the array once.
#Space complexity: O(1)
#as we use only a constant amount of extra space for variables res, curMax, and curMin. We don't use any additional data structures.