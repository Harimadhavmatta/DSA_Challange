# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def middleNode(self, head):
        """
        :type head: ListNode
        a:rtype: ListNode
        """
        slow_pointer=head
        fast_pointer=head
        while fast_pointer and fast_pointer.next :
            fast_pointer=fast_pointer.next.next
            slow_pointer=slow_pointer.next
        return slow_pointer
