class Solution {
    int strStr(String haystack, String needle) =>
      !haystack.contains(needle) ? -1 : haystack.indexOf(needle);
}