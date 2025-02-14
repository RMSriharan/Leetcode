class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=[]
        for j in matrix:
            for i in j:
                l.append(i)
        if target in l:
            return True
        else:
            return False