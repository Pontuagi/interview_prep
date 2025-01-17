"""
# hard 

# Sliding window

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.



Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].



Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.

"""

# solution 

from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        function that returns the starting indices of all the substrings
        with concatenation of all words.
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_map = Counter(words)
        n = len(s)
        result = []

        # iterate over each possible starting position
        for i in range(word_len):
            l = i
            r = i
            c_map = Counter()
            count = 0

            while r + word_len <= n:
                # extract a word from the string
                word = s[r:r + word_len]
                r += word_len

                if word in word_map:
                    c_map[word] += 1
                    count += 1

                    # If word frequency exceed expected count, shrink window.
                    while c_map[word] > word_map[word]:
                        left_word = s[l:l + word_len]
                        c_map[left_word] -= 1
                        count -= 1
                        l += word_len

                    # if all words match, append the starting index to result
                    if count == word_count:
                        result.append(l)

                else:
                    # reset window if word is invalid
                    c_map.clear()
                    count = 0
                    l = r

        return result
