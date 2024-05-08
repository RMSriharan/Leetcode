class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=s.lower()
        alpha='abcdefghijklmnopqrstuvwxyz'
        num='0123456789'
        l=[]
        for i in t:
            if i in alpha or i in num:
                l.append(i)
        w=''.join(l)
        rev=w[::-1]
        if w==rev:
            return True
