class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        u=s[::-1].strip()
        l=u.split(" ")
        return len(l[0])