class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        res=[0]
        index=0
        while(index<n):
            if res[-1]<n:
                res.append(pow(3,index))
                index+=1
            else:
                break
        flag=0
        for i in range(0,len(res)):
            com=combinations(res,i)
            for j in list(com):
                if sum(list(j))==n:
                    flag=1
                    break
        if flag==1:
            return True
        else:
            return False