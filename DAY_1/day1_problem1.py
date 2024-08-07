#   Product of Array Except Self

class Solution(object):
    
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[1]*len(nums)
        left=1
        for i in range(len(ans)):
            ans[i]=left
            left=nums[i]*left
        right = 1
        
        for i in range(len(ans) - 1, -1, -1):
            ans[i] *= right
            right*= nums[i]
        return ans