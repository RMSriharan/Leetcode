class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a=set(nums)
        l=[i for i in a if nums.count(i)==1]
        return l