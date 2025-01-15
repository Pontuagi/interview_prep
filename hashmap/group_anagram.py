"""
# medium

Given an array of strings strs, group the
anagrams
 together. You can return the answer in any order.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]



Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

# Solution

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together from a given list of strings

        Args:
            List[str] - list of strings to group together
        Returns:
            List[List[str]] - list of anagramns grouped together.
        """
        anagrams = defaultdict(list)

        for word in strs:
            # sort words
            sorted_words = ''.join(sorted(word))
            # append original words to corresponding key
            anagrams[sorted_words].append(word)

        return list(anagrams.values())
