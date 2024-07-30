class Solution:
    def minimumDeletions(self, s: str) -> int:
        return s.count('b')-reduce(lambda a,b:max(0,a+(-1)**('a'==b)),s,0)