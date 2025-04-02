long long maximumTripletValue(int* nums, int numsSize) {
    long long int max=0;
    for(int i=0;i<numsSize;i++){
        for(int j=i+1;j<numsSize;j++){
            for(int k=j+1;k<numsSize;k++){
                long long int y=nums[i]-nums[j];
                long long int res=0;
                if(y>0){
                    long long int x=y*nums[k];
                    res=x;
                }
                if(max<res){
                    max=res;
                }
            }
        }
    }
    return max;
    
}