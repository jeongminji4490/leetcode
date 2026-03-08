class Solution {
  bool isPalindrome(int x) {
    String converted = x.toString().split('').reversed.join();
    return converted == x.toString();
  }
}
