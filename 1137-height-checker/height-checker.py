class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort=sorted(heights)
        count=0
        for i in range(0,len(heights)):
            if heights[i]!=sort[i]:
                count+=1
        return count
