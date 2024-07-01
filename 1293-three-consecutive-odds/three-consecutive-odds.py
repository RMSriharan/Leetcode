class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        result=[]
        for i in range(0,len(arr)-2):
            if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0:
                result.append(arr[i])
                result.append(arr[i+1])
                result.append(arr[i+2])
                break
        return result