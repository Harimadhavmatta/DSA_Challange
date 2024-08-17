class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_first(nums, target):
            i, j = 0, len(nums) - 1
            while i <= j:
                mid = (i + j) // 2
                if nums[mid] < target:
                    i = mid + 1
                elif nums[mid] > target:
                    j = mid - 1
                else:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    j = mid - 1
            return -1
        
        def find_last(nums, target):
            i, j = 0, len(nums) - 1
            while i <= j:
                mid = (i + j) // 2
                if nums[mid] < target:
                    i = mid + 1
                elif nums[mid] > target:
                    j = mid - 1
                else:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    i = mid + 1
            return -1
        
        first_pos = find_first(nums, target)
        if first_pos == -1:
            return [-1, -1]
        
        last_pos = find_last(nums, target)
        return [first_pos, last_pos]
