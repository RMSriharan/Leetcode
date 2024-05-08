from itertools import combinations
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count=0
        com=combinations(nums,2)
        for i in list(com):
            y=sum(list(i))
            if y<target:
                count+=1
        return count
