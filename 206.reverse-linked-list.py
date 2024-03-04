#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while(cur):
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre
# @lc code=end

#Time Complexity: O(n)
#Space Complexity: O(1)