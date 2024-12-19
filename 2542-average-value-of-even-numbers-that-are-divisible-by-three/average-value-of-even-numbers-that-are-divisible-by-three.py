class Solution:
    def averageValue(self, nums: List[int]) -> int:
        l=[i for i in nums if i%2==0 and i%3==0]
        if len(l)==0:
            return 0
        else:
            return sum(l)//len(l)