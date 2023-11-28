'''
Given a string s, find the length of the longest substring without repeating characters.


Problem link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

# Brute Force with set
# TC: O(n*26)  SC:O(n*26)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Check if length of string is 0
        if len(s) == 0:
            return 0

        # Initilise the longest length with 1 as it also include string with space
        longestSubStrLength = 1

        # Iterate the string 
        for i_idx in range(0, len(s)):
            # Initialise the set
            subStrSet = set()

            # Check all combinations, it will iterate at max 26 every time 
            # in worst case as there are 26 characters
            for j_idx in range(i_idx, len(s)):
                # Check if character is already in set or not
                if s[j_idx] in subStrSet:
                    break
                else:
                    subStrSet.add(s[j_idx])

            # Update the length    
            longestSubStrLength = max(longestSubStrLength, len(subStrSet))

        # return longest substring length
        return longestSubStrLength

# Sliding Window
# TC: O(n) SC: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Check if length of string is 0
        if len(s) == 0:
            return 0

        # Initilise the longest length with 0
        longestSubStrLength = 0

        # Initialise start and end pointer
        start, end = 0, 0

        # Initialise the hashmap(dict)
        charDict = {}

        # Iterate over the string till the right pointer reaches the end of the string 
        while end < len(s):
            # Increment the count of the character present in the right pointer 
            if s[end] in charDict:
                charDict[s[end]] += 1
            else:
                charDict[s[end]] = 1

            # If the occurence becomes more than 1 means the char is repeated
            while charDict[s[end]] > 1:
                # Reduce the occurence by removing start pointer value from dict
                charDict[s[start]] -= 1
                # Increase the start pointer 
                start += 1

            # As the index starts from 0, length will be (right pointer - left pointer + 1)
            # Update the longest sub string 
            longestSubStrLength = max(longestSubStrLength, end - start  + 1)
            end += 1

        # return longest substring length
        return longestSubStrLength