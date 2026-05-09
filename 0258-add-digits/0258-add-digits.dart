class Solution {
  int addDigits(int num) {
    while (num >= 10) {
        int sum = 0;

        while (num > 0) {
            sum += num % 10; // 8 // 3 // 1 // 2
            num ~/= 10; // 3 // 0 // 1 // 0
        }

        num = sum; // 2
    } 
    return num;
  }
}