class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l,h=nums[:n],nums[n:]
        result=[]
        for i in range(0,len(l)):
            result.append(l[i])
            result.append(h[i])
        return result
