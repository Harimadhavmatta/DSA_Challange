#    3some
class Solution(object):
    def threeSum(self, nums):
       
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        lis=[]
        n=len(nums)
        for i in range(n):
            target=-nums[i]
            if(i>0 and nums[i]==nums[i-1]):
                continue
            left=i+1
            right=n-1
            while(left<right):
                sum=nums[left]+nums[right]
                if(sum==target):
                    lis.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while(left<right and nums[left]==nums[left-1]):
                        left+=1
                    while(left<right and nums[right]==nums[right+1]):
                        right-=1
                elif(target>sum):
                    left=left+1
                else:
                    right=right-1
                    
                
                    
        return lis
