class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod=10**9+7
        main_result=[k for k in nums]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                r=sum(nums[i:j+1])
                main_result.append(r)
        t=sorted(main_result)
        return sum(t[left-1:right])%mod