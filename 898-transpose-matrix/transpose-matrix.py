class Solution:
    def me(self,matrix,i):
        y=[]
        for j in matrix:
            y.append(j[i])
        return y

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result=[]
        for i in range(0,len(matrix[0])):
            t=self.me(matrix,i)
            result.append(t)
        return result