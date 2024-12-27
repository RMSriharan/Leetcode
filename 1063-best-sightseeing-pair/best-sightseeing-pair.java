class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        int n=values.length;
        int isite=values[0]+0;
        int maxscore=0;
        for(int i=1;i<n;i++){
            maxscore=Math.max(maxscore,isite+values[i]-i);
            isite=Math.max(isite,values[i]+i);
        }
        return maxscore;
    }
}