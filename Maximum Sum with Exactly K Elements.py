class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums=sorted(list(set(nums)))
        l=[nums[len(nums)-1]]
        for i in range(0,k-1):
            k=1+nums[len(nums)-1]
            nums[len(nums)-1]=k
            l.append(k)
        return sum(l)
