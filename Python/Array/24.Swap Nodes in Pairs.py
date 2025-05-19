# Solutioin 1:
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution(object):
    def swapPairs(self, head):
        # dummy = ListNode(0, head): dummy is meant to behave as an extra node that sits right before the real list.
        head = ListNode(0, head) # next already points to the real head
        cur = head

        while cur.next and cur.next.next:
            former = cur.next
            latter = former.next

            cur.next = latter
            former.next = latter.next
            latter.next = former

            cur = former

        return head.next

'''
class Solution(object):
    def swapPairs(self, head):
        head = listNode(0, head)
        curr = head


        while a.next and b.next:
            a = curr.next
            b = a.next

            curr.next = b
            a.next = b.next
            b.next = a

            curr = a
        
        return head.next
'''


# Solution 2:
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        
        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head

        return new_head

