class Solution {
  bool isPalindrome(String s) {
    String cleaned = s
    .toLowerCase()
    .replaceAll(RegExp(r'[^a-z0-9]'), '');
    String reversed = '';
    for (int i=cleaned.length-1; i>=0; i--) {
        reversed += cleaned[i];
    }
    return cleaned == reversed;
  }
}