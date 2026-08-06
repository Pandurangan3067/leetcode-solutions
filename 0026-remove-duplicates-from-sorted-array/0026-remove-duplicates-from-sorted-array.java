class Solution {
    public int removeDuplicates(int[] nums) {
        int i,n=nums.length;
        int k=1;
        for (i=1;i<n;i++){
            if( nums[i]!=nums[i-1]){
                nums[k++]=nums[i];
            }
        }
        return k;
    }
}