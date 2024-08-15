class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        nums.reverse()
        if k <= len(nums):
            return nums[k-1]
        return nums[0]

# Example usage:
# sol = Solution()
# result = sol.findKthLargest(nums, k)
