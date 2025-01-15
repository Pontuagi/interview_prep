"""
# easy

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.


Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false



Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.

"""

# solution

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Function that determines if a string s follow a given pattern.
        """
        words = s.split()
        if len(words) != len(pattern):
            return False

        c_to_w = {}
        w_to_c = {}

        for char, word in zip(pattern, words):
            if char in c_to_w:
                if c_to_w[char] != word:
                    return False
            else:
                c_to_w[char] = word

            if word in w_to_c:
                if w_to_c[word] != char:
                    return False
            else:
                w_to_c[word] = char
        return True

# solution 2

class Solution:
        def wordPattern(self, pattern: str, s: str) -> bool:

                s = s.split()

                return (len(set(pattern)) ==
                        len(set(s)) ==
                        len(set(zip_longest(pattern,s))))
