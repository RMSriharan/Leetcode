class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l=[]
        first_row='qwertyuiop'
        second_row='asdfghjkl'
        third_row='zxcvbnm'
        for i in words:
            y=list(set(i.lower()))
            count1,count2,count3=0,0,0
            for j in first_row:
                if j in y:
                    count1+=1
            for k in second_row:
                if k in y:
                    count2+=1
            for t in third_row:
                if t in y:
                    count3+=1
            if count1==len(y):
                l.append(i)
            if count2==len(y):
                l.append(i)
            if count3==len(y):
                l.append(i)
        return l

