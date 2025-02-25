class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix,total=0,0
        mod=10**9+7
        odd,even=0,1
        for i in arr:
            prefix+=i
            if prefix%2!=0:
                total=(total+even)%mod
                odd+=1
            else:
                total=(total+odd)%mod
                even+=1
        return total
        