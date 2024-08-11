class Solution(object):
        def missingNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            s=min(nums)
            b=max(nums)
            for i in range(0,b+1):
                if i not in nums:
                    return i
            return i+1