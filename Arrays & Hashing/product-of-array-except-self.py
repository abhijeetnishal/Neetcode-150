'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Problem link: https://leetcode.com/problems/product-of-array-except-self/description/


Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

# Solution: https://leetcode.com/problems/product-of-array-except-self/solutions/1342916/3-minute-read-mimicking-an-interview/

# Using brute force
# TC: O(n*n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arrLength = len(nums)
        ans = []

        for i_idx in range(0, arrLength):
            prod: int = 1
            
            for j_idx in range(0, arrLength):
                if i_idx != j_idx:
                    prod *= nums[j_idx]

            ans.append(prod)

        return ans

# Using prefix and suffix product without using division
# TC: O(N) SC: O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arrLength = len(nums)
        ans = []

        prefProd = [0] * arrLength
        suffProd = [0] * arrLength

        for idx in range(0, arrLength):
            if idx == 0:
                prefProd[idx] = nums[idx]
            else:
                prefProd[idx] = prefProd[idx-1] * nums[idx]

        for idx in range(arrLength - 1, -1, -1):
            if idx == arrLength - 1:
                suffProd[idx] = nums[idx]
            else:
                suffProd[idx] = suffProd[idx + 1] * nums[idx]

        for idx in range(0, arrLength):
            if idx == 0:
                ans.append(suffProd[idx + 1])
            elif idx == arrLength - 1:
                ans.append(prefProd[idx - 1])
            else:
                ans.append((prefProd[idx - 1]) * (suffProd[idx + 1]))

        return ans

# Space optimised solution
class Solution:
    def productExceptSelf(self, nums):
        n, ans, suffix_prod = len(nums), [1]*len(nums), 1
        for i in range(1,n):
            ans[i] = ans[i-1] * nums[i-1]

        for i in range(n-1,-1,-1):
            ans[i] *= suffix_prod
            suffix_prod *= nums[i]
            
        return ans