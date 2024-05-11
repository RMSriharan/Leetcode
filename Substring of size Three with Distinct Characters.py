class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result=[]
        for i in range(0,len(s)-2):
            t=s[i:i+3]
            if len(set(t))==3:
                result.append(t)
        return len(result)
        
