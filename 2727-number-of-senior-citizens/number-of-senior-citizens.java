class Solution {
    public int countSeniors(String[] details) {
        int count=0;
        for(int i=0;i<details.length;i++){
            String u=details[i];
            int y=Integer.parseInt(u.substring(11,13));
            if (y>60){
                count+=1;
            }
        }
        return count;
    }
}