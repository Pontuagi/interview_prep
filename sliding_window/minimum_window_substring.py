"""
# hard

# Sliding window approach

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

"""

# solution

from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Function that returns the minimum window os substring of s such that
        every a character of t is included. 
        Return:
            The minimum window substring of s
        """
        if not s or not t:
            return ""
        
        t_count = Counter(t)
        required = len(t_count)

        # initialize sliding window pointers
        l, r = 0, 0
        window_count = defaultdict(int)

        formed = 0
        min_len = float('inf')
        result = (0, 0)

        while r < len(s):
            char = s[r]
            window_count[char] += 1

            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            # shrink the window
            while l <= r and formed == required:
                char = s[l]

                # update result if this window is smaller
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    result = [l, r]

                # remove left most character from the window.
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1

                l += 1

            # expand the window
            r += 1
        
        return "" if min_len == float('inf') else s[result[0]:result[1] + 1]
