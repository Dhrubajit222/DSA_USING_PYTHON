'''242. Valid Anagram
Easy
Topics
premium lock icon
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        fre1 = {}
        
        if len(s) != len(t):
            return False
        
        for i in s:
            fre1[i] = fre1.get(i, 0) + 1

        for i in t:
            if i in fre1:
                fre1[i] -= 1
            else:
                return False
            
        for i in fre1.values():
            if i != 0:
                return False
        return True
        

sol = Solution()
s = "ab"
t = "aa"
print(sol.isAnagram(s,t))