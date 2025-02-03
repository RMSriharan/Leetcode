class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_row=[0,0]
        for i in range(0,len(mat)):
            y=mat[i].count(1)
            if max_row[1]==y and max_row[0]>i:
                max_row=[i,y]
            elif max_row[1]==y and max_row[0]<i:
                max_row=max_row
            else:
                if max_row[1]<y:
                    max_row=[i,y]
        return max_row

