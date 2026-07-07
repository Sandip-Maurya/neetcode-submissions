class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0
        m = len(s)
        for ch in t:
            if i < m and ch == s[i]:
                i += 1
            
        return i == m