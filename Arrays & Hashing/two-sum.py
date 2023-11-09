'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Problem link: https://leetcode.com/problems/two-sum/description/


Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
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

# Using sorting
# TC: O(n*log(n))
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arrLength = len(nums)
        
        numsIndexPair = []
        ans = []

        for idx in range(0, arrLength):
            numsIndexPair.append((nums[idx], idx))
        
        numsIndexPair.sort()

        start, end = 0, arrLength - 1

        while start < end:
            if numsIndexPair[start][0] + numsIndexPair[end][0] == target:
                ans = [ numsIndexPair[start][1], numsIndexPair[end][1] ]
                start += 1
                end -= 1
            elif numsIndexPair[start][0] + numsIndexPair[end][0] > target:
                end -= 1
            else:
                start += 1
        
        return ans

# Using Hashmap(Dictionary)
# TC: O(n) SC: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arrLength = len(nums)
        
        ans = []

        numsDict = {}

        for idx in range(0, arrLength):
            numsDict[nums[idx]] = idx

        for idx in range(0, arrLength):
            if target - nums[idx] in numsDict and idx != numsDict[target - nums[idx]]:
                ans = [idx, numsDict[target - nums[idx]]]
        
        return ans