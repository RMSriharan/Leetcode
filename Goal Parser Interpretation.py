class Solution:
    def interpret(self, command: str) -> str:
        y=command.replace("()",('o'))
        t=y.replace("("," ")
        u=t.replace(")"," ")
        e=u.split()
        result=''
        for i in e:
            result+=i
        return result
