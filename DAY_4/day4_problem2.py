# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp=op=None

        while(list1!=None and list2!=None):
            node1=node2=None
            if(list1.val<list2.val):
                node1=list1
                list1=list1.next
            elif(list1.val>list2.val):
                node1=list2
                list2=list2.next
            else:
                node1=list1
                node2=list2
                list1=list1.next
                list2=list2.next
            if node1 and node2:
                if op==None:
                    temp=op=node1
                    temp.next=node2
                    temp=node2
                else:
                    temp.next=node1
                    temp.next.next=node2
                    temp=node2
            elif node1:
                if op==None:
                    temp=op=node1
                    temp=node1
                else:
                    temp.next=node1
                    temp=node1
        if list1 is not None:
            if temp is not None:
                temp.next = list1
            else:
                op = list1 
        if list2 is not None:
            if temp is not None:
                temp.next = list2
            else:
                op = list2 
        return op

