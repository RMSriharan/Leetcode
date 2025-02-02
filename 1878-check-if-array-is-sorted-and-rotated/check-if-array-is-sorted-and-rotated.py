class Solution:
    def check(self, nums: List[int]) -> bool:
        t=sorted(nums)
        i=0
        while i<len(nums):
            w=[t[-1]]+t[0:len(t)-1]
            if w==nums:
                return True
                break
            t=w
            i+=1
        return False
