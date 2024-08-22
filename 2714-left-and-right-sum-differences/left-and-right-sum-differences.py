class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        leftsum,rightsum=[],[]
        rev=nums[::-1]
        for i in range(0,n):
            leftsum.append(sum(nums[0:i]))
            rightsum.append(sum(rev[0:i]))
        v=rightsum[::-1]
        main_result=[abs(leftsum[k]-v[k]) for k in range(0,n)]
        return main_result