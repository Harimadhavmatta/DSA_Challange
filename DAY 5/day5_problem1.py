class Solution(object):
        def isAnagram(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            if(len(s)==0 or len(t)==0):
                return False
            hash1={}
            hash2={}
            for i in s:
                if i in hash1:
                    hash1[i]=hash1[i]+1
                else:
                    hash1[i]=1
            for j in t:
                if j in hash2:
                    hash2[j]=hash2[j]+1
                else:
                    hash2[j]=1
            print(hash1)
            print(hash2)
            if len(hash2)>len(hash1):
                temp=hash2
                hash2=hash1
                hash1=temp
            for k in hash1:
                if k not in hash2:
                    return False
                else:
                    if hash1[k]!=hash2[k]:
                        return False
            return True