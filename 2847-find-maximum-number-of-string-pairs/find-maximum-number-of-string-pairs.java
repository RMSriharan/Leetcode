class Solution {
    public int maximumNumberOfStringPairs(String[] words) {
        int count=0;
        StringBuilder r=new StringBuilder();
        for(int i=0;i<words.length;i++){
            for(int j=i+1;j<words.length;j++){
                r.setLength(0);
                r.append(words[j]);
                if(words[i].equals(r.reverse().toString())){
                    count+=1;
                }
            }
        }
        return count;
    }
}