class Solution:
    def transponse(self,matrix,y):
        h=[]
        for j in matrix:
            h.append(j[y])
        return h

    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        c,k=[],[]        
        trans_mat=[]
        y=0
        for i in matrix:
            c.append(min(i))
        for i in range(0,len(matrix[0])):
            x=self.transponse(matrix,y)
            y+=1
            trans_mat.append(x)
        for i in trans_mat:
            k.append(max(i))
        if max(c)==min(k):
            return [min(k)]
    
   