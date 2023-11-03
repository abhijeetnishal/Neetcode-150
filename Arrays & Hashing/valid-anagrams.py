'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

# Using sorting
# TC: O(n*log(n))
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t

# Using hashmap
# TC: O(n) SC: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = [0] * 26

        # Count the frequency of characters in string s
        for char in s:
            hashmap[ord(char) - ord('a')] += 1
        
        # Decrement the frequency of characters in string t
        for char in t:
            hashmap[ord(char) - ord('a')] -= 1

        # Check if any character has non-zero frequency
        for val in hashmap:
            if val:
                return False
        
        return True