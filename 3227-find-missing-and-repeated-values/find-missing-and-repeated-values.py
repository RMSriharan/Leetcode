class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        new=[i for i in range(1,len(grid)*len(grid)+1)]
        ext,miss=[],[]
        w=[]
        for i in grid:
            for j in i:
                w.append(j)
        for k in list(set(w)):
            if w.count(k)>1:
                ext.append(k)
        for h in new:
            if h not in w:
                miss.append(h)
        return ext+miss