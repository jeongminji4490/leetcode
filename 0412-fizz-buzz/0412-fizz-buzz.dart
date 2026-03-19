class Solution {
  List<String> fizzBuzz(int n) {
    List<String> result = [];
    for (int i=1; i<=n; i++) {
        result.add(_getString(i));
    }
    return result;
  }

  String _getString(int n) {
    if (n%3 == 0 && n%5 == 0) {
        return 'FizzBuzz';
    } else if (n%3 == 0) {
        return 'Fizz';
    } else if (n%5 == 0) {
        return 'Buzz';
    } else {
        return n.toString();
    }
  }
}