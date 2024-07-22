class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l=sorted([[heights[i],names[i]] for i in range(0,len(names))])[::-1]
        result=[i[1] for i in l]
        return result