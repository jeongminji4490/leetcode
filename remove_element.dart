int removeElement(List<int> nums, int val) {
  int k = 0;

  for (int i = 0; i < nums.length; i++) {
    if (nums[i] != val) {
      nums[k] = nums[i];
      k++;
    }
  }
  return k;
}

void main(List<String> arguments) {
  print(removeElement([3, 2, 2, 3], 3));
}
