"""
# medium

Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

"""

# solution

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Function to return all elements of the matrix in spiral order
        """
        res = []

        if not matrix:
            return res

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        #traverse the matrix in layers
        while top <= bottom and left <= right:
            # traverse from left to right
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # traverse from top to bottom
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # traverse from right to left if applicable
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            
            # traverse from bottom to top if applicable
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1
        return res
