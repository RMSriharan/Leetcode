class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        main=[]
        s=[]
        for i in score:
            s.append(i[k])
        w=sorted(s)[::-1]
        for j in w:
            for t in score:
                if t[k]==j:
                    main.append(t)
        return main