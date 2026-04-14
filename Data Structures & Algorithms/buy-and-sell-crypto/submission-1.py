class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R, profit = 0, 1, 0

        while R < len(prices):
            if prices[R] > prices[L]:
                profit = max(profit, prices[R] - prices[L])
            else:
                L = R
            
            R += 1
        
        return profit
        