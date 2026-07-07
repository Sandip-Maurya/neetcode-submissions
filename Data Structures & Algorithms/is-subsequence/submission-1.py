class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        m = len(s)
        if m > n:
            return False
        if m == 0:
            return True
            
        sub_string = ""
        s_temp = s
        t_temp = t
        
        for i in range(n):
            if not s_temp:
                break
            if t[i] == s_temp[0]:
                sub_string += t[i]
                s_temp = s_temp[1:]
            t_temp = t_temp[1:]
        return sub_string == s