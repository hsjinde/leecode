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
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell
        return profit
        
# @lc code=end

# O(n)

