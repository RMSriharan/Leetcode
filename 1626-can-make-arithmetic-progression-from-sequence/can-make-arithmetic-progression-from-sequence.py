class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        y=sorted(arr)
        l=[]
        for i in range(0,len(arr)-1):
            x=abs(y[i+1]-y[i])
            l.append(x)
        if len(set(l))==1:
            return True