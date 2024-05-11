class Solution:
    def repeatedCharacter(self, s: str) -> str:
        l=sorted(list(set(s)))
        k=0
        result=[]
        while(k<len(l)):
            q=[]
            for i in range(0,len(s)):
                if l[k]==s[i]:
                    q.append(i)
            if len(q)>=2:
                result.append(q[1])
            k+=1
        return s[min(result)]
