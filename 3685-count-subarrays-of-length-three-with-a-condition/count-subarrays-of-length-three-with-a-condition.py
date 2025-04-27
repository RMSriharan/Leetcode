class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count=0
        for i in range(0,len(nums)-2):
            x=nums[i:i+3]
            if x[1]%2==0:
                if x[0]+x[2]==(x[1]//2):
                    count+=1
        return count