class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        r=[]
        for i in arr:
            if arr.count(i)==1:
                r.append(i)
        if len(r)<k-1 or len(r)==0:
            return ""
        else:
            return r[k-1]