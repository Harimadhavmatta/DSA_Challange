class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0:
                return []
        op=[]
        dic={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],
        7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        def backtrack(i,it):
            if i==len(digits):
                op.append("".join(it))
                return
            for x in dic[int(digits[i])]:
                it.append(x)
                backtrack(i+1,it)
                it.pop()
        it=[]
        backtrack(0,it)
        return op
