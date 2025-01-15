"""
# medium 

# Sliding window technique

Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

# solution 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Function to find the longest substring without repeating characters
        """
        char_set = set()
        l = 0
        max_l = 0

        for r in range(len(s)):
            # if char in char_set, shrink window from the left.
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            # add current char to set
            char_set.add(s[r])
            max_l = max(max_l, r - l + 1)

        return max_l