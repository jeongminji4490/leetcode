class Solution {
  int firstUniqChar(String s) {
    Map<String, int> map = {};
    for (int i=0; i<s.length; i++) {
        map[s[i]] = (map[s[i]] ?? 0) + 1;
    }
    if (map.containsValue(1)) {
        final key = map.entries.firstWhere((e) => e.value == 1).key;
        return s.indexOf(key);
    } else {
        return -1;
    }
  }
}