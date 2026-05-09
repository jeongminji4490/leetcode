class Solution {
  List<int> numberGame(List<int> nums) {
    nums.sort();

    List<int> result = [];

    for (int i=0; i<nums.length; i+=2) {
        result.add(nums[i+1]);
        result.add(nums[i]);
    }

    return result;
  }
}