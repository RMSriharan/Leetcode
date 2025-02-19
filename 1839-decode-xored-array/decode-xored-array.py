class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr=[first]
        for i in range(0,len(encoded)):
            x=arr[i]^encoded[i]
            arr.append(x)
        return arr