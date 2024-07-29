class Solution:
    def maximum69Number (self, num: int) -> int:
        t=str(num)
        if '6' not in t:
            return num
        else:
            w=[i for i in t]
            result=[]
            for i in range(0,len(t)):
                if w[i]=='6':
                    w[i]='9'
                    r=int(''.join(w))
                    result.append(r)
                    w[i]='6'
                else:
                    w[i]='6'
                    r=int(''.join(w))
                    result.append(r)
                    w[i]='9'
            return max(result)