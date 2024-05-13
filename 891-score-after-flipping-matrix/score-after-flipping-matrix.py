class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        nrows,ncols=len(grid),len(grid[0])
        def fliprow(row):
            for col in range(ncols):
                grid[row][col]=1-grid[row][col]
        def flipcol(col):
            for row in range(nrows):
                grid[row][col]=1-grid[row][col]
        def checkrow(nums):
            return int(''.join([str(num)for num in nums]),2)
        for row in range(nrows):
            if grid[row][0]==0:
                fliprow(row)
        for col in range(ncols):
            if sum(grid[r][col]for r in range(nrows))*2<nrows:
                flipcol(col)
        return sum(checkrow(row)for row in grid)