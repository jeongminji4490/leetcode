class Solution {
  bool isAnagram(String s, String t) {
    if (s.length != t.length) return false;
    // use map
    // r = 1 a = 1 t = 1
    Map<String, int> smap = {};
    for (int i=0; i<s.length; i++) {
        smap[s[i]] = (smap[s[i]] ?? 0) + 1;
    } 
    // c = 1 a = 1 r = 1
    Map<String, int> tmap = {};
    for (int i=0; i<t.length; i++) {
        tmap[t[i]] = (tmap[t[i]] ?? 0) + 1;
    }
    for (final key in smap.keys) {
        if (tmap[key] == null || (tmap[key] != smap[key])) {
            return false;
        }
    }
    return true;
  }
}