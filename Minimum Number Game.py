class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        r=sorted(nums)
        result=[]
        for i in range(0,len(nums),2):
            result.append(r[i+1])
            result.append(r[i])
        return result
