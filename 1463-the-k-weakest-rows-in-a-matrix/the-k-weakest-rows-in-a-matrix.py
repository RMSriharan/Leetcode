class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l=[[mat[i].count(1),i] for i in range(0,len(mat))]
        w=[j[1] for j in sorted(l)][:k]
        return w