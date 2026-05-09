class Solution {
  bool checkIfPangram(String sentence) {
    Map<String, int> map = {};
    for (int i=0; i< sentence.length; i++) {
        map[sentence[i]] = (map[sentence[i]] ?? 0) + 1;
    }
    if (map.keys.length == 26) {
        return true;
    } else {
        return false;
    }
  }
}