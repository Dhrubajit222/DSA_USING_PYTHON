'''1920. Build Array from Permutation
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

 

Example 1:

Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
Explanation: The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]
Example 2:

Input: nums = [5,0,1,2,3,4]
Output: [4,5,0,1,2,3]
Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] < nums.length
The elements in nums are distinct.
 

Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?'''

class Solution(object):
    def buildArray(self, nums):
        """
        LeetCode 1920: Build Array from Permutation

        Given:
            nums is a permutation of numbers from 0 to n-1.

        We have to create a new array 'ans' such that:

            ans[i] = nums[nums[i]]

        Time Complexity : O(n)
        Space Complexity: O(n)
        """

        # Create a new list by visiting each index.
        # For every index i:
        #   1. nums[i] gives another index.
        #   2. nums[nums[i]] gives the value at that new index.
        return [nums[nums[i]] for i in range(len(nums))]


# Create an object of Solution class
s = Solution()

# Take space-separated integers as input
# Example Input:
# 0 2 1 5 3 4
nums = list(map(int, input("Enter the permutation: ").split()))

# Print the resulting array
print("Output:", s.buildArray(nums))

