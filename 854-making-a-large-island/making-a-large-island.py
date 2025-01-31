class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def dfs(i,j,mark):
            grid[i][j]=mark
            dirs=[(1,0),(0,1),(-1,0),(0,-1)]
            curr_size=1
            for dx,dy in dirs:
                x,y=i+dx,j+dy
                if -1<x<m and -1<y<n and grid[x][y]==1:
                    curr_size+=dfs(x,y,mark)
            return curr_size
        has_zero=False
        mark=2
        island_sizes=defaultdict(int)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    island_sizes[mark]=dfs(i,j,mark)
                    mark+=1
                elif grid[i][j]==0:
                    has_zero=True
        if not has_zero:
            return m*n
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    unique_islands=set()
                    dirs=[(1,0),(0,1),(-1,0),(0,-1)]
                    for dx,dy in dirs:
                        x,y=i+dx,j+dy
                        if 0<=x<m and 0<=y<n and grid[x][y]>1:
                            unique_islands.add(grid[x][y])
                    candidate_size=1
                    for island in unique_islands:
                        candidate_size+=island_sizes[island]
                    res=max(res,candidate_size)
        return res