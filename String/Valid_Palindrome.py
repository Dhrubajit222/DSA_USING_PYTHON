'''125. Valid Palindrome
Solved
Easy
Topics
premium lock icon
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left = 0
        right = len(s) - 1
        while left < right:
            left_ch = s[left].lower()
            right_ch = s[right].lower()
            
            if not left_ch.isalnum():
                left += 1
            elif not right_ch.isalnum():
                right -= 1
            elif left_ch != right_ch:
                return False
            else:
                left += 1
                right -= 1

        return True


            

sol = Solution()
s = input()
print(sol.isPalindrome(s))
