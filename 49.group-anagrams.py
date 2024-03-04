#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        res = []
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in mp:
                mp[sorted_s] = len(res)
                res.append([s])
            else:
                res[mp[sorted_s]].append(s)
        return res

# @lc code=end

#Time complexity: O(n∗k∗logk)
#Space complexity:  O(n∗k∗logk)