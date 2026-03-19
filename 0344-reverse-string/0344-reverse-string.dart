class Solution {
  void reverseString(List<String> s) {
    var lastIdx = s.length-1;
    for (int idx=0; idx<s.length/2; idx++) {
        if (idx == lastIdx) break;
        final f = s[idx];
        final b = s[lastIdx];
        s[idx] = b;
        s[lastIdx] = f;
        lastIdx--;
    }
  }
}