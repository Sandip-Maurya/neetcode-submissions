class Solution:
    def scoreOfString(self, s: str) -> int:
        m = len(s)
        score = 0
        for i in range(m-1):
            score += abs(ord(s[i])-ord(s[i+1]))
        return score