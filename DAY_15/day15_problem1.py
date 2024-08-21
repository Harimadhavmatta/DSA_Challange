class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        q = deque()

        for idx, num in enumerate(nums):
            while q and q[-1] < num:
                q.pop()
            q.append(num)

            if idx >= k and nums[idx - k] == q[0]:
                q.popleft()
            
            if idx >= k - 1:
                res.append(q[0])
        return res