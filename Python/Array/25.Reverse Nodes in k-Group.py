# Solution 1:
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverse(self, start, end):
        pre, curr = None, start
        while curr != end:
            nexts = curr.next
            curr.next = pre
            pre = curr
            curr = nexts
        return pre

    def reverseKGroup(self, head, k):
        count, temp = 0, head
        while temp and count < k:
            temp = temp.next
            count += 1

        if count < k:
            return head
        
        new_head = self.reverse(head, temp)
        head.next = self.reverseKGroup(temp, k)

        return new_head


# Solution 2:
class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = left = right = head

        while True:
            count = 0
            # Move right k steps ahead
            while right and count < k:
                right = right.next
                count += 1

            if count == k:
                prev, curr = right, left
                # Reverse k nodes
                for _ in range(k):
                    nexts = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nexts
                # Connect with previous part
                jump.next = prev
                # Move jump and left to the next group
                jump = left
                left = right
            else:
                return dummy.next

