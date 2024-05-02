class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        y=[i for i in word]
        if ch not  in word:
            return word
        else:
            t=y.index(ch)
            w,q=y[:t+1][::-1],y[t+1:]
            u=''.join(w+q)
            return u
