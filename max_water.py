"""
# medium 

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

"""
# solution 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Function to return the max area of container with most water
        """
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            water = width * min(height[left], height[right])
            max_water = max(max_water, water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

## more efficient solution

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Function to return the max area of container with most water
        """
        left, right = 0, len(height) - 1
        max_water = 0
        highest = max(height)

        while left < right:
            # width = right - left
            # reduce space.
            water = (right - left) * min(height[left], height[right])
            # max_water = max(max_water, water)
            if water > max_water:
                max_water = water

            # make the code more efficient
            if highest * (right - left) < max_water:
                break

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
