class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        numTracker=0
        minIncrement=0
        for num in nums:
            numTracker=max(numTracker,num)
            minIncrement+=numTracker-num
            numTracker+=1
        return minIncrement