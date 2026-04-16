class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count, window = [0] * 26, [0] * 26
        L, k = 0, len(s1)

        for c in s1:
            count[ord(c) - ord('a')] += 1
        
        for R in range(len(s2)):
            window[ord(s2[R]) - ord('a')] += 1

            if (R - L + 1) > k:
                 window[ord(s2[L]) - ord('a')] -= 1
                 L += 1

            if (R - L + 1) == k and window == count:
                return True
        
        return False

        