"""
# medium 

Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

"""

# solution

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Function to calculate the minimum size of a sub array whose
        sum add up to the target value.
        Arguments:
            Target - the value to achieve through addition
            nums - array containing positive integers
        return:
            length of subarray whose value is greater or equal to target
            0 - the target cannot be achieved.
        """
        left = 0
        addition = 0
        min_length = float('inf')

        for i in range(len(nums)):
            addition += nums[i]

            while addition >= target:
                min_length = min(min_length, i - left + 1)
                addition -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0
