"""
# easy

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

"""
# solution

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Function to check if ransomNote can be constructed using letters from magazine
        Returns:
            True: if true
            False:
        """
        # count frequency of characters in magazine
        mag_count = Counter(magazine)

        # check each character in ransomNote
        for char in ransomNote:
            if mag_count[char] <= 0:
                return False

            mag_count[char] -= 1

        return True
