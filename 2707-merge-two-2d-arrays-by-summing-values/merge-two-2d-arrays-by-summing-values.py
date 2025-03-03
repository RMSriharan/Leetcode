class Solution:
    def find(self,nums1:List[List[int]],nums2:List[List[int]])->List[List[int]]:
        set1=[]
        for i in nums1:
            flag=0
            for j in nums2:
                if i[0]==j[0]:
                    flag=1
                    break
            if flag==0:
                set1.append(i)
        return set1
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        x=self.find(nums1,nums2)
        y=self.find(nums2,nums1)
        res=[]
        for i in nums1:
            for j in nums2:
                if i[0]==j[0]:
                    res.append([i[0],i[1]+j[1]])
        return sorted(res+x+y)