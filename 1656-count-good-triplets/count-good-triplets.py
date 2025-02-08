class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res=[]
        com=combinations(arr,3)
        for i in list(com):
            x=list(i)
            if abs(x[0]-x[1])<=a and abs(x[1]-x[2])<=b and abs(x[0]-x[2])<=c:
                res.append(x)
        return len(res)