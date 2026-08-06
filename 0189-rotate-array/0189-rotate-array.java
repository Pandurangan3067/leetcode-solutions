class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;

        k = k % n;

        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1);
    }

    private void reverse(int[] nums, int left, int right) {
        while (left < right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;

            left++;
            right--;
        }
    }
}
/* 
 * MATH THEORY: Think of the array as two blocks, A (first n-k elements) and B (last k elements). We start with [A, B] and want [B, A].
 * 1. Reversing the entire array is like doing (AB)^R, which gives us [B^R, A^R] — the blocks are swapped, but internally backwards.
 * 2. Reversing the first block (B^R)^R and the second block (A^R)^R fixes them, leaving us with exactly [B, A].
 */