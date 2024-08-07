class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt=Counter(word)
        lst=sorted(cnt,key=lambda x:-1*cnt[x])
        ct=0
        x=1
        tot=0
        for i in lst:
            tot+=(cnt[i]*x)
            ct+=1
            if ct==8:
                x+=1
                ct=0
        return tot
        return 0