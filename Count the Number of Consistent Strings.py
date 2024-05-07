class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        l=[]
        for i in words:
            count=0
            for j in i:
                if j in allowed:
                    count+=1
            if count==len(i):
                l.append(i)
        return len(l)
