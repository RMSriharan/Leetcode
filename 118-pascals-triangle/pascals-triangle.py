class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        else:
            result=[[1],[1,1]]
            for i in range(1,numRows-1):
                t=result[i]
                y=[]
                for j in range(0,len(t)-1):
                    e=t[j]+t[j+1]
                    y.append(e)
                w=[t[0]]+y+[t[len(t)-1]]
                result.append(w)
            return result