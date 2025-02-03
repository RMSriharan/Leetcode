class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new=[i[::-1] for i in image]
        w=[]
        for j in new:
            q=[]
            for k in j:
                if k==1:
                    q.append(0)
                else:
                    q.append(1)
            w.append(q)
        return w