# Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution(object):
        def hasCycle(self, head):
            """
            :type head: ListNode
            :rtype: bool
            """
            hash={}
            while(head):
                if head in hash:
                    return True
                hash[head]=head.next
                head=head.next
            return False