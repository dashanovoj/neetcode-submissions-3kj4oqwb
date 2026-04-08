class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_low, k_high = 1, max(piles)

        while k_low < k_high:
            k = (k_low + k_high) // 2
            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k
            
            if hours <= h:
                k_high = k
            else:
                k_low = k + 1
        
        return k_low
        