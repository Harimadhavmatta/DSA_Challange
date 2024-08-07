#             Search a 2D Matrix

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        point=None
        previous_max=matrix[0][0]
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        if len(matrix[0]) == 1:
            for i in matrix:
                if i[0]==target:
                    return True
            
        for i in matrix:
            max=i[-1]
            if(previous_max<=target and max>=target):
                point=i
                break
            previous_max=max

        if point is not None:
            print(point)
            return target in point
            
        return False
        
        