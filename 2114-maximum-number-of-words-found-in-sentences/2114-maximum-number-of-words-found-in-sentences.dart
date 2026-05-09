class Solution {
  int mostWordsFound(List<String> sentences) {
    List<int> result = [];
    for (int i=0; i<sentences.length; i++) {
        result.add(sentences[i].split(" ").length);
    }
    return result.reduce((a, b) => a > b ? a : b);
  }
}