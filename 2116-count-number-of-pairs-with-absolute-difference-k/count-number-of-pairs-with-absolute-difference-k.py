class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                x,y=nums[i],nums[j]
                w=abs(x-y)
                if w==k:
                    count+=1
        return count