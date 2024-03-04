#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        opcl = dict(('()', '[]', '{}'))
        stack = []
        for symbol in s:
            if symbol in '([{':
                stack.append(symbol)
            elif len(stack) == 0 or symbol != opcl[stack.pop()]:
                return False
        return len(stack) == 0
# @lc code=end

