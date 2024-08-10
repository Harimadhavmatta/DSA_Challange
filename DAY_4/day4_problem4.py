class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp=[target-i for i in nums]
        print(nums)
        print(temp)
        for i in range(len(nums)):
            if(nums[i] in temp and i!=temp.index(nums[i])):
                j=temp.index(nums[i])
                return [i,j]
        
        return []