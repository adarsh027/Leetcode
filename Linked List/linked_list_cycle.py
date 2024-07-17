# ref: https://www.youtube.com/watch?v=gBTe7lFR3vc
# ref: https://leetcode.com/problems/linked-list-cycle/description/
class Solution:
    def hasCycle(self, head):
        slow, fast = head, head
      
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False