class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        x,y,z=[i for i in nums if i<pivot],[j for j in nums if j==pivot],[k for k in nums if k>pivot]
        return x+y+z