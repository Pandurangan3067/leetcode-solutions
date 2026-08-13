class Solution {
    public void sortColors(int[] nums) {
        int l=0,m=0,h=nums.length-1;
        int t;
        while(m<=h){
            if(nums[m]==0){
                t=nums[l];
                nums[l]=nums[m];
                nums[m]=t;
                l++;
                m++;
            }
            else if(nums[m]==1)
                m++;
            else{
                t=nums[m];
                nums[m]=nums[h];
                nums[h]=t;
                h--;
            }
        }
    }
}