class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        l=[]
        for i in range(low,high+1):
            r=str(i)
            if len(r)%2==0:
                s1,s2=0,0
                n1,n2=r[0:len(r)//2],r[len(r)//2:len(r)]
                for j in range(0,len(r)//2):
                    s1+=int(n1[j])
                    s2+=int(n2[j])
                if s1==s2:
                    l.append(i)
        return len(l)
