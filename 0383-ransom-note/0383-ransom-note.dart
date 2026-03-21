class Solution {
  bool canConstruct(String ransomNote, String magazine) {
    final m = magazine.split('');
    for (final r in ransomNote.split('')) {
        if (!m.contains(r)) return false;
        m.remove(r);
    }
    return true;
  }
}