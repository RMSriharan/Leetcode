class UF:
    def __init__(self,n):
        self.n=n
        self.par=[i for i in range(n+1)]
        self.rank=[1]*(n+1)

    def find(self,x):
        p=self.par[x]
        while p!=self.par[p]:
            self.par[p]=self.par[self.par[p]]
            p=self.par[p]
        return p

    def union(self,x1,x2):
        p1,p2=self.find(x1),self.find(x2)
        if p1==p2:
            return 0
        if self.rank[p1]>self.rank[p2]:
            self.rank[p1]+=self.rank[p2]
            self.par[p2]=p1
        else:
            self.rank[p2]+=self.rank[p1]
            self.par[p1]=p2
        self.n-=1
        return 1
    def ic(self):
        return self.n==1
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a,b=UF(n),UF(n)
        c=0
        for t,s,d in edges:
            if t==3:
                c+=(a.union(s,d)|b.union(s,d))
        for t,s,d in edges:
            if t==1:
                c+=a.union(s,d)
            if t==2:
                c+=b.union(s,d)
        if a.ic() and b.ic():
            return len(edges)-c
        return -1