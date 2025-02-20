class Solution:
    #def find(self)
    def getLucky(self, s: str, k: int) -> int:
        l=[chr(i) for i in range(97,123)]
        r=''
        for j in s:
            r+=str(l.index(j)+1)
        q=[int(i) for i in r]
        w=[]
        for i in range(0,k):
            w.append(sum(q))
            q=[int(i) for i in str(sum(q))]
        return w[-1]