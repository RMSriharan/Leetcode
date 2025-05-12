from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        perm=permutations(digits,3)
        l=[]
        h=list(set(perm))
        for i in h:
            res=''
            for k in i:
                res+=str(k)
            v=str(int(res))
            if len(v)==3:
                if int(v)%2==0:
                    l.append(int(v))
        return sorted(l)

        