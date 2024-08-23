class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        max1=[]
        new_grid=[sorted(i) for i in grid]
        index=len(grid[0])-1
        while(len(max1)<len(grid[0])):
            k=[]
            for u in new_grid:
                k.append(u[index])
            index-=1
            max1.append(max(k))
        return sum(max1)