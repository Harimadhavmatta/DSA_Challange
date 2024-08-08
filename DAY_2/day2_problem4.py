#           := search insert position (easy)
class Solution(object):
    def binary(self , nums,target):
        l=0
        n=len(nums)
        r=n-1
        while(l<=r):
            mid=(l+r)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                l=mid+1
            else:
                r=mid-1
        
        return l 
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans=self.binary(nums,target)

        return ans
