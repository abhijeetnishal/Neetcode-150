'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.


Problem link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
'''

# Brute Force
# TC: O(n*n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arrLength = len(nums)
        ans = []

        for i_idx in range(0, arrLength - 1):
            for j_idx in range(i_idx + 1, arrLength):
                if nums[i_idx] + nums[j_idx] == target:
                    ans = [i_idx, j_idx]
                
        return ans

# Using Two Pointer Approach
# TC: O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        ans = []

        while start < end:
            if numbers[start] + numbers[end] == target:
                ans = [start + 1, end + 1]
                start += 1
                end -= 1
            elif numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1

        return ans