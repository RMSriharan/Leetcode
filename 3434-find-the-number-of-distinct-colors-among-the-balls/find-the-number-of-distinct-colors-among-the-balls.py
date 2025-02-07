class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_d=defaultdict(list)
        ball_d=defaultdict(int)
        ans=[]
        for ball,color in queries:
            color_d[color].append(ball)
            if ball in ball_d:
                c=ball_d[ball]
                color_d[c].remove(ball)
                if len(color_d[c])==0:
                    color_d.pop(c)
            ball_d[ball]=color
            ans.append(len(color_d))
        return ans