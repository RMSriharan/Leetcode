class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length=len(nums[0])
        y=sorted([int(i,2) for i in nums])
        res=[]
        count=0
        while True:
            if count in y:
                count+=1
            else:
                x=bin(count)[2:]
                if len(x)<length:
                    res.append('0'*(length-len(x))+x)
                    break
                else:
                    res.append(x)
                    break
        return res[-1]