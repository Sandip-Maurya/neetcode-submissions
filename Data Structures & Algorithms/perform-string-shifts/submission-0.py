class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        def _shift_letter(string: str, direction: int) -> str:
            if direction == 1: # right shift
                return s[-1] + s[:-1]
            else:
                return s[1:] + s[0] 
        

        for direction_i, amount_i in shift:
            if amount_i == 0:
                continue
            for i in range(1, amount_i+1):
                s = _shift_letter(s, direction_i)
        return s

