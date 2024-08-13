class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l=0
        r=len(s)-1
        s=list(s)
        while(l<r):
            if(s[l]==s[r]):
                continue
            else:
                print("--------")
                temp=s[l]
                s[l]=s[r]
                s[r]=temp
                print('s[L] : ',s[l])
                print('s[r] : ',s[r])
            l=l+1
            r=r-1
        return "".join(s)
