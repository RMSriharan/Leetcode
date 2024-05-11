class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        t=sorted(list(set(nums)))
        l=[]
        for i in t:
            if nums.count(i)%2==0:
                l.append(nums.count(i))
        if len(l)==len(t):
            return True
