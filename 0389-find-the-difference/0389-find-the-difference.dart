class Solution {
  String findTheDifference(String s, String t) {
    final tcopy = t.split('');
    for (int i=0; i<s.length; i++) {
        tcopy.remove(s[i]);
    }
    return tcopy.first;
  }
}