class Solution {
  bool isIsomorphic(String s, String t) {
    final Map<String, int> mapS = {};
    final Map<String, int> mapT = {};

    for (int i = 0; i < s.length; i++) {
      String cs = s[i];
      String ct = t[i];

      if (mapS[cs] != mapT[ct]) return false;

      mapS[cs] = i;
      mapT[ct] = i;
    }

    return true;
  }
}