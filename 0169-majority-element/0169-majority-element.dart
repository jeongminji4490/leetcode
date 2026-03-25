class Solution {
  int majorityElement(List<int> nums) {
    final minFrequency = nums.length / 2;
    Map<int, int> map = {};

    for (int i=0; i<nums.length; i++) {
        map[nums[i]] = (map[nums[i]] ?? 0) + 1;
        if ((map[nums[i]] ?? 0) > minFrequency) {
            return nums[i];
        }
    }
    return -1;
  }
}