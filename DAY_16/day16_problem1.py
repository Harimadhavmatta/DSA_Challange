class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        col = set()
        pos_dia = set()
        nag_dia = set()

        def backtrack(r):
            if r == n:
                self.count += 1
                return
            for c in range(n):
                if c in col or r + c in pos_dia or r - c in nag_dia:
                    continue
                col.add(c)
                pos_dia.add(r + c)
                nag_dia.add(r - c)
                backtrack(r + 1)
                col.remove(c)
                pos_dia.remove(r + c)
                nag_dia.remove(r - c)
        
        backtrack(0)
        return self.count
