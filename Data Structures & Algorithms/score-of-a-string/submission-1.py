class Solution:
    def scoreOfString(self, s: str) -> int:
        m = len(s)
        score = 0
        import math
        for i in range(m-1):
            first = ord(s[i])
            second = ord(s[i+1])
            # score += (first-second) if first - second >=0 else (second-first)
            score += abs(first-second)
        return score