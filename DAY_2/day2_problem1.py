# sliding window
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_lis=[]
        if(len(nums)==0):
            return max_lis
        if(len(nums)<k):
            max_lis.append(max(nums))
            return max_lis
       
        for i in range(len(nums)-(k-1)):
            max_lis.append(max(nums[i:i+k]))
        print(max_lis)
        return max_lis
