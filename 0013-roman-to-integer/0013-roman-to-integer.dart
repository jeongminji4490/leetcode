class Solution {
  int romanToInt(String s) {
    final map = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000,
    };

    int result = 0;

    for (int i = 0; i < s.length; i++) {
      final current = map[s[i]]!;
      if (i < s.length - 1 && current < map[s[i + 1]]!) {
        result -= current;
      } else {
        result += current;
      }
    }
    return result;
  }
}