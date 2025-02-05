class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        else:
            flag=0
            t=[i for i in s1]
            for i in range(0,len(s1)):
                for j in range(i+1,len(s1)):
                    temp=t[i]
                    t[i]=t[j]
                    t[j]=temp
                    r=''.join(t)
                    if r==s2:
                        flag=1
                        break
                    else:
                        temp=t[i]
                        t[i]=t[j]
                        t[j]=temp
            if flag==1:
                return True
            else:
                return False