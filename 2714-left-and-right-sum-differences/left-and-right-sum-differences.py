class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        leftsum=[]
        rightsum=[]
        rev=nums[::-1]
        for i in range(0,n):
            leftsum.append(sum(nums[0:i]))
        for j in range(0,n):
            rightsum.append(sum(rev[0:j]))
        v=rightsum[::-1]
        main_result=[]
        for k in range(0,n):
            main_result.append(abs(leftsum[k]-v[k]))
        return main_result