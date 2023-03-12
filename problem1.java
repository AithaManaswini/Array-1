// time complexity - O(n)
// space complexity - O(n)
//  Did this code successfully run on Leetcode :yes
// Three line explanation of solution in plain english
// to solve this problem, we can find the product of left subarray and the product
// of right subarray and multiply them to get the result of product without the number itself
// Your code here along with comments explaining your approach
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] left = new int[nums.length];
        int[] right = new int[nums.length];
        int[] res = new int[nums.length];
        // product of left subarray
        for (int i =0;i<nums.length;i++){
            if (i==0){
                left[i] = 1;
            }
            else{
                left[i] = left[i-1]*nums[i-1];
            }
        }
        // product of right subarray
        for (int i =nums.length-1;i>=0;i--){
            if (i==nums.length-1){
                right[i] = 1;
            }
            else{
                right[i] = right[i+1]* nums[i+1];
            }
        }
        // product of left and right subarrays
         for (int i =0;i<nums.length;i++){
             res[i] = left[i] * right[i];
         }

    return res;
        
        
    }
}