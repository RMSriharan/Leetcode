class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        t=sentence.split()
        vowels='aeiuoAEIUO'
        result,index=[],2
        for i in t:
            if i[0] in vowels:
                result.append(i+'m'+'a'*index)
            else:
                result.append(i[1:]+i[0]+'m'+'a'*index)
            index+=1
        return ' '.join(result)