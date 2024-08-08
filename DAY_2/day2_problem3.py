#             first missing positive (hard)
class Solution(object):
    def insertion(self,nums):
        n=len(nums)
        for i in range(1,n):
            for j in range(i):
                if(nums[i]<nums[j]):
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==1 and nums[0]!=1):
            return 1
        elif(len(nums)==1):
            return nums[0]+1
        self.insertion(nums)
        small=nums[-1]
        large=nums[0]
        print(nums)
        x=0
        hash={}
        while(len(nums)!=0):
            if (nums[x]<=0):
                nums.pop(x)
            else:
                break
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]]=1
            else:
                hash[nums[i]]+=1
        print(hash)
        d=1
        while(d):
            if d not in hash:
                return d
            d=d+1
        return d

