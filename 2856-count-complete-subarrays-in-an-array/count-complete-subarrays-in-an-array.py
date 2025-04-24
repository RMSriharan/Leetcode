class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        tot=len(set(nums))
        n=len(nums)
        res,l,fre=0,0,defaultdict(int)
        for rig in range(n):
            fre[nums[rig]]+=1
            while len(fre)==tot:
                res+=n-rig
                fre[nums[l]]-=1
                if fre[nums[l]]==0:
                    del fre[nums[l]]
                l+=1
        return res