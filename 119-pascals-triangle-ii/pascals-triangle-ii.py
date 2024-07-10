class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result=[[1],[1,1]]
        for i in range(1,rowIndex):
            t=result[i]
            y=[]
            for j in range(0,len(t)-1):
                e=t[j]+t[j+1]
                y.append(e)
            w=[t[0]]+y+[t[len(t)-1]]
            result.append(w)
        return result[rowIndex]