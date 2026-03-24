class Solution {
  bool containsDuplicate(List<int> nums) {
    Map<int, int> map = {};
    for (int i=0; i<nums.length; i++) {
        map[nums[i]] = (map[nums[i]] ?? 0) + 1;
        if ((map[nums[i]] ?? 0 ) == 2) return true;
    }
    return false;
  }
}