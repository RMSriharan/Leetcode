class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l,m=[],[]
        for i in s:
            if i.isalpha()==True:
                l.append(i)
                m.append(" ")
            else:
                m.append(i)
        g,k=l[::-1],0
        for j in range(0,len(m)):
            if m[j]==" ":
                m[j]=g[k]
                k+=1
        return ''.join(m)
