''' 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Problem link: https://leetcode.com/problems/valid-parentheses/description/


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

# Using Stack
# TC: O(n)  SC: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        # Length of string s
        strLength = len(s)
        # Create a list named stack
        stack = []

        # Iterate list
        for idx in range(0, strLength):
            # Only pop out the elements from stack if stack is not empty and
            # Only pop out the elements if current value is closing bracket and 
            # stack top is opening bracket corresponding to same closing bracket
            if len(stack) > 0 and ((s[idx] == ')' and stack[-1] == '(') or (s[idx] == '}' and stack[-1] == '{') or (s[idx] == ']' and stack[-1] == '[')):
                stack.pop()
            # Else add element at the top of stack
            else:
                stack.append(s[idx])

        # if stack is empty meaning it is valid else it is not valid
        return len(stack) == 0