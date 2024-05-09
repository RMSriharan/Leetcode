class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result=max([sum(i) for i in accounts])
        return result
