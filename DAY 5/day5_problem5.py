class Solution(object):
        def singleNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            first=[]
            sec=[]
            for i in nums:
                if i not in first:
                    first.append(i)
                else:
                    sec.append(i)
            return list(set(first) - set(sec))[0]