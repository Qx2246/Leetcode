# Solution 1:
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        # revursive function to create a linked-list head (ListNode); 
        # if simply use left = lists[:mid], merge function  will fail as it is a list not listNode.
        left = self.mergeKLists(lists[:mid]) 
        right = self.mergeKLists(lists[mid:])

        return self.merge(left, right)

    
    def merge(slef, l1, l2):
        head = ListNode(0)
        curr = head

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 or l2

        return head.next



# Solution 2:
def mergeKLists(self, lists):
        values = []
        
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next
        
        values.sort()
        
        head = ListNode(0)
        current = head
        
        for val in values:
            current.next = ListNode(val)
            current = current.next
        
        return head.next

