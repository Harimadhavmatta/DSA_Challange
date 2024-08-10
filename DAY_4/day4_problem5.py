class Solution(object):
    def check(self,d):
        i=0
        j=len(d)-1
        while(i<=j):
            if(d[i]==d[j]):
                i=i+1
                j=j-1
            else:
                return False
        return True
        
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        flat=""
        for i in s:
            if (i.isalpha() or i.isnumeric()):
                flat=flat+i
        print(flat)
        if(self.check(flat)):
            return True
        return False
