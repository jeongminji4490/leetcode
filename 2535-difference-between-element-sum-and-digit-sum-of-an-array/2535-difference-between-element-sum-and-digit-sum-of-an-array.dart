class Solution {
  int differenceOfSum(List<int> nums) {
    int esum = 0;
    int dsum = 0;

    for (final num in nums) {
        esum += num;

        int n = num;

        while (n > 0) {
            dsum += n%10;
            n ~/= 10;
        }
    }

    return (esum - dsum).abs();
  }
}