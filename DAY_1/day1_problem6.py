#        contains duplicate


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic={}
        count=1
        for i in nums:
            if i not in dic:
                dic[i]=count
            else:
                return True
        return False
        