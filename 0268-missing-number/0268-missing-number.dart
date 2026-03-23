class Solution {
  int missingNumber(List<int> nums) {
    int sum = 0;
    for (int i=0; i<nums.length+1; i++) {
        sum += i;
    }
    int i=nums.length-1;
    while (i >= 0) {
        sum -= nums[i];
        i--;
    }
    return sum;
  }
}