class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        op=[]
        def backtrack(i,it):
            if(i==len(nums)):
                op.append(it[:])
                return
            it.append(nums[i])
            backtrack(i+1,it)

            it.pop()
            backtrack(i+1,it)
        backtrack(0,[])
        return op