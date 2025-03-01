class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        main,zero=[i for i in nums if i!=0],[i for i in nums if i==0]
        return main+zero