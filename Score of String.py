class Solution:
    def scoreOfString(self, s: str) -> int:
        l=[]
        for i in range(0,len(s)-1):
            x,y=ord(s[i]),ord(s[i+1])
            t=abs(x-y)
            l.append(t)
        return sum(l)
