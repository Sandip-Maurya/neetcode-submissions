class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid_digits = {2, 3, 4, 5, 7}
        digit_count = len(str(abs(n)))
        reversed_number = 0
        n_temp = n 
        while n_temp:
            n_temp, digit = divmod(n_temp, 10)
            if digit in invalid_digits:
                return False
            if digit == 6:
                digit = 9
            elif digit == 9:
                digit = 6
            reversed_number += digit*10**(digit_count-1)
            digit_count -=1
        
        if reversed_number == n:
            return False
        return True
