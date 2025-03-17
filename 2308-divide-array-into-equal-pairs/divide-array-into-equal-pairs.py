class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n=len(nums)//2
        new=sorted(nums)
        count=0
        for i in range(0,len(nums)-1,2):
            x=new[i:i+2]
            if len(set(x))==1:
                count+=1
        if count==n:
            return True
        else:
            return False