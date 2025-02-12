class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        h=defaultdict(list)
        max1=-1
        for n in nums:
            sum1=sum(list(map(int,str(n))))
            h[sum1].append(n)
        for k,v in h.items():
            if len(v)>=2:
                max1=max(sum(sorted(v)[::-1][:2]),max1)
        return max1