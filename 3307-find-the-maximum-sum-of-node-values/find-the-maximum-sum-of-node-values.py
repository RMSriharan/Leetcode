class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        maxSum=sum(max(num,num^k) for num in nums)
        changedcount=sum((num^k)> num for num in nums)
        if changedcount%2==0:
            return maxSum
        minchangeddiff=min(abs(num-(num^k)) for num in nums)
        return maxSum-minchangeddiff