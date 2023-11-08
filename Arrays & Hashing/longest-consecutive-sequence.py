'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Problem link: https://leetcode.com/problems/longest-consecutive-sequence/description/


Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

# Using sorting
# TC: O(n*log(n))
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arrLength = len(nums)

        if arrLength == 0:
            return 0

        nums.sort()

        cnt = 1
        longestSeq = 0

        for idx in range(1, arrLength):
            if nums[idx - 1] + 1 == nums[idx]:
                cnt += 1
            elif nums[idx] != nums[idx - 1]:
                longestSeq = max(cnt, longestSeq)
                cnt = 1
        
        longestSeq = max(cnt, longestSeq)

        return longestSeq

# TC: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for n in num_set:
            if (n-1) not in num_set:
                length = 1
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest