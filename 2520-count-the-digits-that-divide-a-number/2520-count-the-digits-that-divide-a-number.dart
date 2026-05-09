class Solution {
  int countDigits(int num) {
    List<int> list = [];
    final s = num.toString();
    for (int i=0; i<s.length; i++) {
        list.add(int.parse(s[i]));
    }
    int sum = 0;
    for (int i=0; i<list.length; i++) {
        if (num%list[i] == 0) sum++;
    }
    return sum;
  }
}