# Solution 1:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class solution(object):
    def removeNthFromEnd_two_pass(head, n):
        length = 0
        cur = head
        # count number of items in head
        while cur:
            length += 1
            cur = cur.next

        remove_index = length - n # if i = 0, then len - n is the index of removal item

        # remove the matched index
        if remove_index == 0:
            return head.next
        else:
            for i in range(remove_index - 1): # stop right before the removal index
                head = head.next
            
        if head.next == head.next: # check if there is an item after the removal index
            head.next = head.next.next
        else:
            None

        return head



# Solution 2: (best way)
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast, slow = head, head

        for _ in range(n): # fast moves first, always n nodes ahead slow
            fast = fast.next

        if not fast: 
            return head.next

        while fast.next:  # 1, 2, 3 (slow), 4, 5(fast); while-loop stops as fast.next is None, so slow is one node before removal index
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next # skip the removal index

        return head
