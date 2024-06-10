class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(0,len(nums)):
            u=bin(i)[2:]
            l=[j for j in u]
            if l.count('1')==k:
                count+=nums[i]
        return count