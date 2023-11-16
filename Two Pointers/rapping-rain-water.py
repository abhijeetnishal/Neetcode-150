'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


Problem link: https://leetcode.com/problems/trapping-rain-water/description/


Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
 
Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''

# Using Greedy 
# TC: O(n) SC: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        maxLeft = [0] * n
        maxRight = [0] * n

        maxLeft[0] = height[0] 
        maxRight[n-1] = height[n-1]

        for idx in range(1, n):
            maxLeft[idx] = max(maxLeft[idx-1], height[idx])
        
        for idx in range(n-2, -1, -1):
            maxRight[idx]=max(maxRight[idx + 1],height[idx])
        
        maxarea = 0

        for idx in range(0, n):
            water = (min(maxLeft[idx], maxRight[idx]) - height[idx])
            maxarea += water

        return maxarea

# Using Two Pointer
# TC: O(n) SC: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) <= 2:
            return 0
        
        ans = 0
        
        #using two pointers start and end on indices 1 and n-1
        start = 1
        end = len(height) - 1
        
        #initialising leftmax to the leftmost bar and rightmax to the rightmost bar
        lmax = height[0]
        rmax = height[-1]
        
        while start <= end:
            # check lmax and rmax for current start, end positions
            if height[start] > lmax:
                lmax = height[start]
            if height[end] > rmax:
                rmax = height[end]
            
            #fill water upto lmax level for index start and move start to the right
            if lmax <= rmax:
                ans += lmax - height[start]
                start += 1
				
            #fill water upto rmax level for index end and move end to the left
            else:
                ans += rmax - height[end]
                end -= 1
                
        return ans