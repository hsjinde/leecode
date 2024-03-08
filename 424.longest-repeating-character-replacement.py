#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen, longestCount = 0,0
        hashmap = collections.Counter()
        for i in range(len(s)):
            hashmap[s[i]] += 1
            longestCount = max(longestCount, hashmap[s[i]] )
            if maxlen - longestCount >= k:
                hashmap[s[i - maxlen]] -= 1
            else:
                maxlen += 1
        return maxlen

# @lc code=end

# Time Complexity :  O(n)
# Space Complexity : O(1)