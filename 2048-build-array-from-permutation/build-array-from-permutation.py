class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        j=0
        while(j<len(nums)):
            ans.append(nums[nums[j]])
            j+=1
        return ans
        