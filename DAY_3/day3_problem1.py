import re
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        lis=re.split(r'[\[\]]',s)
        lis=list(filter(None,lis))
        print(lis)
        result=""
        for i in range(0,len(lis)-1,2):
            
            result=result+lis[i+1]*int(lis[i])
            print(result)
            print(i+1)
        return result