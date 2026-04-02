class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        max_amount = 0
        while L < R:
            amount = (R - L) * min(heights[R], heights[L])
            max_amount = max(max_amount, amount)

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
            
        return max_amount
        