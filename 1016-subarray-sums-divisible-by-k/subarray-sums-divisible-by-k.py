class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        running=count=0
        remainder=collections.defaultdict(int)
        remainder[0]=1
        for num in nums:
            running+=num
            if running%k in remainder:
                count+=remainder[running%k]
            remainder[running%k]+=1
        return count