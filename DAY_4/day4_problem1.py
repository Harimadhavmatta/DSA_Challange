from collections import deque
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=deque()
        op=["[","{","("]
        cl=["}","]",")"]
        dic={')':'(', '}': '{', ']' :'[',}
        if(len(s)<=1):
            return False
        for i in s:
            if i in op:
                stack.append(i)

            elif i in cl and len(stack)==0:
                return False
            else:
                if stack.pop()!=dic[i]:
                    return False
        if(len(stack)!=0):
            return False
        return True
        

