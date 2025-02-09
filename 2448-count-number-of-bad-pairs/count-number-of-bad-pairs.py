class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        counter={}
        for i in range(len(nums)):
            counter[nums[i]-i]=counter.get(nums[i]-i,0)+1
        n=len(nums)
        tot=(n*(n-1))//2
        good=0
        for freq in counter.values():
            if freq>1:
                good+=(freq*(freq-1))//2
        return tot-good