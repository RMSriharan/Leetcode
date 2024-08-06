class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        main_result=[]
        for i in range(lo,hi+1):
            count=0
            u=i
            while(i!=1):
                if i%2==0:
                    i=i//2
                    count+=1
                else:
                    i=3*i+1
                    count+=1
            main_result.append([count,u])
        t=sorted(main_result)[k-1]
        return t[1]