class Solution(object):
        def majorityElement(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            if(len(nums)==1):
                return nums[0]
            hash={}
            for i in nums:
                if i not in hash:
                    hash[i]=1
                elif(i in hash):
                    hash[i]=hash[i]+1
                    if(hash[i]>=len(nums)//2+1):
                        return i
            return -1