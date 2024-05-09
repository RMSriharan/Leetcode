class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n=len(s)
        dp=[0]*n
        for i in range(0,n):
            dp[indices[i]]=s[i]
        return ''.join(dp)
