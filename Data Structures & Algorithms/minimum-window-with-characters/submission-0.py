class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        count = [0] * 128
        L, need = 0, len(t)
        min_len, start = float("inf"), 0
        
        for c in t:
            count[ord(c)] += 1
        
        for R in range(len(s)):
            if count[ord(s[R])] > 0:
                need -= 1
            count[ord(s[R])] -= 1

            while need == 0:
                if (R - L + 1) < min_len:
                    min_len = R - L + 1
                    start = L

                count[ord(s[L])] += 1
                if count[ord(s[L])] > 0:
                    need += 1
                
                L += 1

        return "" if min_len == float("inf") else s[start:start + min_len]