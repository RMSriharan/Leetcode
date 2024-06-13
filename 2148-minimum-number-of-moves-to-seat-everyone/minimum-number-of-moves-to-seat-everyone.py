class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        count=0
        x,y=sorted(seats),sorted(students)
        for i in range(0,len(x)):
            h=abs(x[i]-y[i])
            count+=h
        return count