class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        flag=0
        b=bin(n)[2:]
        for i in range(0,len(b)-1):
            if b[i]==b[i+1]:
                flag=1
                break
        if flag==1:
            return False
        else:
            return True