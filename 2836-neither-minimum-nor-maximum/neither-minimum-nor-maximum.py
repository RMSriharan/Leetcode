class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)==1:
            return -1
        else:
            nums.remove(min(nums))
            nums.remove(max(nums))
            if len(nums)==0 :
                return -1
            else:
                return nums[0]