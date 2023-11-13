''' 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Problem Link: https://leetcode.com/problems/3sum/description/ 


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

# Brute Force
# TC: O(n*n*n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arrLength = len(nums)

        ans = []


        for i_idx in range(0, arrLength - 2):
            for j_idx in range(i_idx + 1, arrLength - 1):
                for k_idx in range(j_idx + 1, arrLength):
                    if nums[i_idx] + nums[j_idx] + nums[k_idx] == 0:
                        # Sort the triplet and add it to the result if not already present
                        triplet = sorted([nums[i_idx], nums[j_idx], nums[k_idx]])
                        
                        if triplet not in ans:
                            ans.append(triplet)

        return ans

# Two Pointer Approach
# TC: O(n*n):
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arrLength = len(nums)

        nums.sort()

        ans = []

        for idx in range(0, arrLength):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            start, end = idx + 1, arrLength - 1
            
            while start < end:
                threeSum = nums[idx] + nums[start] + nums[end]

                if threeSum == 0:
                    ans.append([nums[idx], nums[start], nums[end]])
                
                    while (start < end) and nums[start] == nums[start + 1]:
                        start += 1
                    
                    while (start < end) and nums[end] == nums[end - 1]:
                        end -= 1

                    start += 1
                    end -= 1

                elif threeSum < 0:
                    start += 1
                
                else:
                    end -= 1

        return ans