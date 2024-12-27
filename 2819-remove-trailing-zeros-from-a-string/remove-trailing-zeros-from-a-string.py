class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        g=str(int(num[::-1]))[::-1]
        return g