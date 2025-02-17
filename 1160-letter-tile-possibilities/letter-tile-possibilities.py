import numpy as np
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt,n,prod,tmp=0,len(tiles),[1],[1]
        for i in range(n): tmp.append(tmp[-1]/(i+1));
        for v in Counter(tiles).values():prod=np.polymul(prod,tmp[v::-1])
        return int(sum((prod[i]*math.factorial(n-i)) for i in range(n)))