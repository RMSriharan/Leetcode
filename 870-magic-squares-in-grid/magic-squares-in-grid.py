class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        cnt=0
        def col(r,c):
            a,b,d=0,0,0
            for i in range(r,r+3):
                a+=grid[i][c]
                b+=grid[i][c+1]
                d+=grid[i][c+2]
            if a==b==d:
                return a
            return -2
        def row(r,c):
            a,b,d=0,0,0
            for i in range(c,c+3):
                a+=grid[r][i]
                b+=grid[r+1][i]
                d+=grid[r+2][i]
            if a==b==d:
                return a
            return -1
        def diagonal(r,c):
            a,b=0,0
            for j in range(3):
                a+=grid[r+j][c+j]
                b+=grid[r+j][c+2-j]
            if a==b:
                return a
            return -3
        def check_numbers(r,c):
            s=set()
            for i in range(3):
                for j in range(3):
                    if 1<=grid[r+i][c+j]<=9:
                        s.add(grid[r+i][c+j])
            return len(s)==9
        for i in range(len(grid)-2):
            for j in range(len(grid[i])-2):
                r=row(i,j)
                d=diagonal(i,j)
                c=col(i,j)
                if r==d==c and check_numbers(i,j):
                    cnt+=1
        return cnt