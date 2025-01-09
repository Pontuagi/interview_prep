"""
## easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

"""

# solution 
# The Boyer-Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Function to find the majority element in an array.
        """
        count = 0
        major_element = 0

        for i in nums:
            if count == 0:
                major_element = i
            if major_element == i:
                count += 1
            else:
                count -= 1

        return major_element
