class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l=[[mat[i].count(1),i] for i in range(0,len(mat))]
        w=sorted(l)
        t=[j[1] for j in w]
        return t[:k]