class Solution:
    def idealArrays(self, n: int, max_value: int) -> int:
        MOD=1_000_000_007
        total=max_value
        fre={num:1 for num in range(1,max_value+1)}
        for arr in range(1,n):
            new=Counter()
            for base in fre:
                for mul in range(2,max_value//base+1):
                    com=comb(n-1,arr)
                    total+=com*fre[base]
                    new[mul*base]+=fre[base]
            fre=new
            total%=MOD
        return total