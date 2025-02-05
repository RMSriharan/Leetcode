class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decomp=[]
        for i in range(0,len(nums),2):
            e=nums[i:i+2]
            f,val=e[0],e[1]
            for j in range(0,f):
                decomp.append(e[1])
        return decomp