class Solution:
    def find(self,mat:List[List[int]],index:int)->List[int]:
        new=[]
        for j in mat:
            new.append(j[index])
        return new[::-1]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new=[]
        for i in range(0,len(matrix)):
            x=self.find(matrix,i)
            new.append(x)
        for j in range(0,len(matrix)):
            matrix[j]=new[j]
        return matrix