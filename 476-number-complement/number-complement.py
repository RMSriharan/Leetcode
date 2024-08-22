class Solution:
    def findComplement(self, num: int) -> int:
        r=str(bin(num))
        t=r[2:]
        l=[]
        for i in t:
            if i=='0':
                l.append('1')
            else:
                l.append('0')
        u=''.join(l)
        decimal=0
        for j in u:
            decimal=decimal*2+int(j)
        return decimal