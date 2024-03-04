#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #O(nlogn)
        #return sorted(s) == sorted(t) 
        count = defaultdict(int)
        for i in s:
            count[i] += 1
        for i in t:
            count[i] -= 1
        for val in count.values():
            if val != 0: 
                return False
        return True

# @lc code=end

