'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

# Brute force
# TC: O(n*n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxmProfit  = 0
        arrLength = len(prices)

        # Iterate list
        for i_idx in range(0, arrLength - 1):
            for j_idx in range(i_idx + 1, arrLength):
                # check all combinations to find mxm profit
                mxmProfit = max(mxmProfit, prices[j_idx] - prices[i_idx])

        return mxmProfit


# Optimised: Greedy or Maths
# TC: O(n) 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arrLength = len(prices)

        sellAmount = prices[arrLength - 1]
        buyAmount = prices[arrLength - 1]
        mxmProfit  = 0

        # Iterate list from 2nd last element
        for idx in range(arrLength - 2, -1, -1):
            # Take current element as buy amount
            # as we need to buy before selling
            buyAmount = prices[idx]

            # Update sell amount as we need mxm profit
            if buyAmount > sellAmount:
                sellAmount = prices[idx]

            # calculate maximum profit 
            mxmProfit = max(mxmProfit, sellAmount - buyAmount)

        return mxmProfit

'''
Dry run:
[7, 1, 5, 3, 6, 4]

sellAmount = 4
buyAmount = 4
profit = 0

sellAmount = 6
buyAmount = 6
profit = 0

sellAmount = 6
buyAmount = 3
profit = 3

sellAmount = 6
buyAmount = 5
profit = 1

sellAmount = 6
buyAmount = 1
profit = 5

sellAmount = 6
buyAmount = 7
profit = -1

mxmProfit = 5
'''