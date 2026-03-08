// Two Sum
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.
// Input: nums = [3,2,4], target = 6
// Output: [1,2]

List<int> twoSum(List<int> nums, int target) {
  bool isFound = false;
  List<int> result = [];
  for (int i = 0; i < nums.length; i++) {
    var left = target - nums[i];
    for (int j = i + 1; j < nums.length; j++) {
      if (left - nums[j] == 0) {
        isFound = true;
        if (isFound) {
          result.add(i);
          result.add(j);
        }
        break;
      }
    }
    if (isFound) break;
  }
  return result;
}

// Refactored
// Use hash map
// Find value matches to complement - subtracted value from target in hash map
List<int> twoSum2(List<int> nums, int target) {
  Map<int, int> map = {};

  for (int i = 0; i < nums.length; i++) {
    int complement = target - nums[i];

    if (map.containsKey(complement)) {
      return [map[complement]!, i];
    }

    map[nums[i]] = i;
  }

  return [];
}

void main(List<String> arguments) {
  print(twoSum2([3, 5, 11, 2], 16));
}
