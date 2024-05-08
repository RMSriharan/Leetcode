class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        y=sorted(score)[::-1]
        t,result=[],[]
        for i in range(0,len(score)):
            x=score[i]
            t.append(y.index(x)+1)
        w=["Gold Medal","Silver Medal","Bronze Medal"]
        for j in t:
            if j==1 or j==2 or j==3:
                result.append(w[j-1])
            else:
                result.append(str(j))
        return result
