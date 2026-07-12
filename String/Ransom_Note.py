'''383. Ransom Note
Easy
Topics
premium lock icon
Companies
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
ransomNote and magazine consist of lowercase English letters.'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        fre = {}
        remining = len(ransomNote)

        for i in ransomNote:
            fre[i] = fre.get(i,0) + 1

        for i in magazine:
            if i in fre and fre[i] > 0:
                fre[i] -= 1
                remining -= 1
            if remining == 0:
                return True
            
        for i in fre.values():
            if i != 0:
                return False
            
        return True

sol = Solution()
ransomNote = input()
magazine = input()
print(sol.canConstruct(ransomNote, magazine))