class Solution {
    public String findDifferentBinaryString(String[] nums) {
       StringBuilder res = new StringBuilder();
       int n = nums.length;
       for(int i = 0 ; i < n ; i++) {
            res.append(nums[i].charAt(i) == '0' ? '1' : '0');
       }
       return res.toString();
    }
}