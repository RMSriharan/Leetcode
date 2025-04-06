class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n=len(nums)
        dp=[[nums[i]]for i in range(n)]
        max_subset=[nums[0]]
        for i in range(1,n):
            for j in range(i):
                if nums[i]%nums[j]==0 or nums[j]%nums[i]==0:
                    if len(dp[i])<len(dp[j])+1:
                        dp[i]=dp[j]+[nums[i]] 
                        if len(dp[i])>len(max_subset):
                            max_subset=dp[i]
        return max_subset       