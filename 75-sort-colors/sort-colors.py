class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)-1):
            m=i
            for j in range(i+1,len(nums)):
                if nums[m]>nums[j]:
                    m=j
            nums[i],nums[m]=nums[m],nums[i]
        return nums