class Solution {
  List<int> twoSum(List<int> nums, int target) {
    List<int> result = [];
    Map<int, int> map = {};
    // var sum = 0;

    for (int i=0; i<nums.length; i++) {
        map[i] = nums[i];
    }

    int i = 0;

    while (i < map.length) {
        var value = map[i] ?? 0;
        var left = target - value;
        for (int j=i+1; j<map.length; j++) {
            if (map[j] == left) {
                result.add(i);
                result.add(j);
                break;
            }
        }
        if (result.length == 2) break;
        i++;
    }

    return result;
  }
}