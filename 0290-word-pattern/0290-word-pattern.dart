class Solution {
  bool wordPattern(String pattern, String s) {
    List<String> list = s.split(' ');
    if (pattern.length != list.length) return false;

    Map<String, String> pToW = {};
    Map<String, String> wToP = {};

    for (int i = 0; i < pattern.length; i++) {
      String p = pattern[i];
      String w = list[i];

      if (pToW.containsKey(p) && pToW[p] != w) return false;
      if (wToP.containsKey(w) && wToP[w] != p) return false;

      pToW[p] = w;
      wToP[w] = p;
    }

    return true;
  }
}