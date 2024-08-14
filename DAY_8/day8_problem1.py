# Climbing Stairs (Easy)
# This solution uses dynamic programming with memoization to store previously computed results and avoid redundant calculations.
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        hash={}
        return self.real(n,hash)
    def real(self,num,memo):
        if(num<=1):
            return 1
        if(num in memo):
            return memo[num]
        else:
            memo[num]=self.real(num-1,memo)+self.real(num-2,memo)
        return memo[num]
