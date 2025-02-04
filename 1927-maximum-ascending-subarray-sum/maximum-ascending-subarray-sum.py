class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        main,temp=[],[]
        for i in range(0,len(nums)-1):
            temp.append(nums[i])
            if nums[i]>=nums[i+1]:
                main.append(sum(temp))
                temp=[]
        temp.append(nums[-1])
        if temp:
            main.append(sum(temp))

        return max(main)