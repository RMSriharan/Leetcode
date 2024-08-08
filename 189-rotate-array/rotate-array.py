class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,k):
            x,y=nums[0],nums[-1]
            nums[0]=y
            nums.pop(len(nums)-1)
            nums.insert(1,x)
        return nums