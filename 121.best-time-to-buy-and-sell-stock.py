#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for price in prices:
            if price - buy > 0:
                profit = max(price - buy, profit)
            else:
                buy = price
        return profit
        
# @lc code=end

# O(n)

