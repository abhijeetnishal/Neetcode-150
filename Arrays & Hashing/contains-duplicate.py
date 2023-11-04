''' 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Problem link: https://leetcode.com/problems/contains-duplicate/

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

# Brute force
# TC: O(n*n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arrLen = len(nums)
        for i_idx in range(0, arrLen):
            for j_idx in range(i_idx + 1, arrLen):
                if nums[i_idx] == nums[j_idx]:
                    return True
                

        return False    

# Using sorting
# TC: O(n*log(n))
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arrLen = len(nums)

        nums.sort()

        for idx in range(0, arrLen - 1):
            if nums[idx] == nums[idx + 1]:
                return True

        return False 

# Using Dictionary(hashmap)
# TC: O(n) SC: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arrLen = len(nums)

        freqDict = {}

        for idx in range(0, arrLen):
            if nums[idx] in freqDict:
                return True

            freqDict[nums[idx]] = 1

        return False 

# Using set
# TC: O(n) SC: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arrLen = len(nums)

        arrSet = set()

        for idx in range(0, arrLen):
            if nums[idx] in arrSet:
                return True
            arrSet.add(nums[idx])

        return False 