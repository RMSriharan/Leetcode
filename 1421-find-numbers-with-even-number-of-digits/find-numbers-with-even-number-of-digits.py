class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l=[i for i in nums if len(str(i))%2==0]
        return len(l)