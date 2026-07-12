class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
                
        for direction_i, amount_i in shift:
            if amount_i == 0:
                continue
            if direction_i == 1: # right shift
                s = s[-amount_i:] + s[:-amount_i]
            else:
                s = s[amount_i:] + s[:amount_i]
            
        return s

