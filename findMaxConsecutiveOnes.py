class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k=[str(i) for i in nums]
        y=''.join(k)
        if '1' not in y:
            return 0
        else:
            t=y.replace('0',' ')
            w=t.split()
            return len(max(w))
