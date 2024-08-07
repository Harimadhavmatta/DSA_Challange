#              Sort Colors


class Solution(object):
    def sort(self,list):
        l=0
        r=l+1
        while(l!=len(list) and r!=len(list)):
            if(list[l]>list[r]):
                list[l],list[r]=list[r],list[l]
            r=r+1
            if(r==len(list)):
                r=l=l+1
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        self.sort(nums)
        