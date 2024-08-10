class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n=len(grid)*3
        mapping={
            " ":[0,0,0,0,0,0,0,0,0],
            "/":[0,0,1,0,1,0,1,0,0],
            "\\":[1,0,0,0,1,0,0,0,1],
        }
        aug_gird=[[0]*n for _ in range(n)]
        def fill_grid(row,column,label):
            i=0
            for r in range(3*row,3*row+3):
                for c in range(3*column,3*column+3):
                    aug_gird[r][c]=mapping[label][i]
                    i+=1
        for r in range(len(grid)):
            for c,label in enumerate(grid[r]):
                fill_grid(r,c,label)
        def dfs(r,c):
            if r<0 or r>=n or c<0 or c>=n or aug_gird[r][c]==1:
                return 0
            aug_gird[r][c]=1
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
            return 1
        res=0
        for r in range(n):
            for c in range(n):
                res+=dfs(r,c)
        return res 