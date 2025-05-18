# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        current = head

        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        current.next = l1 or l2
        '''if l1:
            current.next = l1
        elif l2:
            current.next = l2'''

        return head.next

