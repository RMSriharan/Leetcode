class Solution:
    def coloredCells(self, n: int) -> int:
        if n==1:
            return 1
        else:
            res=[1]
            for i in range(0,n):
                x=res[-1]+(4*i)
                res.append(x)
            return res[-1]