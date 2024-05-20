class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sumtotal=0
        for num in nums:
            sumtotal|=num
        return sumtotal<<(len(nums)-1)