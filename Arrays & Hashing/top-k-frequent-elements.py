'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Problem link: https://leetcode.com/problems/top-k-frequent-elements/description/


Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

# Using sorting (dictionary with lambda function)
# TC: O(n*log(n))
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}

        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1

        sortedList = list(sorted(freqDict.items(), key=lambda item: item[1], reverse=True))
        
        ans = []

        for idx in range(0, k):
            ans.append(sortedList[idx][0])

        return ans


# Using Heap
# TC: n*log(k)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}

        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1

        heap = []

        for key in freqDict.keys():
            if len(heap) == k: # If size is k then we dont want to increase the size further 
                heapq.heappushpop(heap, (freqDict[key], key))
            else: # Size is not k then freely push values
                heapq.heappush(heap, (freqDict[key], key))

		# After this operation the heap contains only k largest values of all the values in nums

        ans = []

        while k > 0:
            k -= 1
            ans.append(heapq.heappop(heap)[1])

        return ans