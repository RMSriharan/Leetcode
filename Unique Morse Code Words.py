class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        l=[]
        alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        transformation=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in words:
            w=[]
            for j in i:
                t=alphabet.index(j)
                w.append(transformation[t])
            y=''.join(w)
            l.append(y)
        result=len(set(l))
        return result
