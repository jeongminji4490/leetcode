class Solution {
  String reverseVowels(String s) {
    final vowels = ['a', 'e', 'i', 'o', 'u'];
    final inputVowels = [];
    String result = '';

    for (int i=s.length-1; i>=0; i--) {
        if (vowels.contains(s[i].toLowerCase())) {
            inputVowels.add(s[i]);
        }
    }

    for (int i=0; i<s.length; i++) {
        if (vowels.contains(s[i].toLowerCase())) {
            result += inputVowels.first;
            inputVowels.removeAt(0);
        } else {
            result += s[i];
        }
    }
    return result;
  }
}