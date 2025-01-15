"""

# medium

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0

        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h_index += 1
            else:
                break

        return h_index
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Function to determine the h_index of a citations arrays.
        arguments:
            citaions: an array containing the numbe of citations for each paper.

        Returns the h_index
        """
        citations.sort(reverse=True)
        h_index = 0

        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h_index += 1
            else:
                break

        return h_index
