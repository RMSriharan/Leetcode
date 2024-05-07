class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]
        for i in operations:
            if i=='C':
                y=len(l)-1
                l.pop(y)
            elif i=='D':
                x=l[len(l)-1]
                l.append(x*2)
            elif i=='+':
                if len(l)>=2:
                    x,y=l[len(l)-1],l[len(l)-2]
                    l.append(x+y)
            else:
                l.append(int(i))
        return sum(l)
        
