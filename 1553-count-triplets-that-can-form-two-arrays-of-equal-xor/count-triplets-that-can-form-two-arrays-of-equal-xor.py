class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans=0
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                a=0
                for k in range(i,j):
                    a^=arr[k]
                b=0
                for m in range(j,n):
                    b^=arr[m]
                    if a==b:
                        ans+=1
        return ans