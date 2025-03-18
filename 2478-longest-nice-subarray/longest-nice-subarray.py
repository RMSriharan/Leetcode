class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        mask,max1,i=0,0,0
        for j in range(len(nums)):
            while((mask&nums[j])!=0):
                mask^=nums[i]
                i+=1
            mask|=nums[j]
            max1=max(max1,j-i+1)
        return max1