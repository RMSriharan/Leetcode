class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    y=nums[i]-nums[j]
                    if y>0:
                        x=y*nums[k]
                        res.append(x)
        if len(res)==0:
            return 0
        else:
            return max(res)