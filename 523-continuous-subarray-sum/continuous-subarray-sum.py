class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_k_prefixes=set()
        prev_prefix_sum=0
        nums[0]%=k
        for prefix_sum in accumulate(nums,lambda a,b:(a+b)%k):
            if prefix_sum in mod_k_prefixes:
                return True
            else:
                mod_k_prefixes.add(prev_prefix_sum)
                prev_prefix_sum=prefix_sum
        return False