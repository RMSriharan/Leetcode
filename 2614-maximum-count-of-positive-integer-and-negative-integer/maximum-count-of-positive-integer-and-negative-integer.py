class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        s=0
        m=0
        for i in nums:
            if i>0:
                s+=1
            if i<0:
                m+=1
        if s>m:
            return s
        else:
            return m

        