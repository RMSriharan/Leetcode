class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(1,len(nums)+1):
            y=nums[0:i]
            result.append(sum(y))
        return result
