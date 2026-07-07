class Solution:
    def confusingNumber(self, n: int) -> bool:
        if n == 0:
            return False
            
        invalid_digits = {2, 3, 4, 5, 7}
        reversed_number = 0
        str_n = str(n)
        length_n = len(str_n)

        for digit in str_n:
            if int(digit) in invalid_digits:
                return False
            if digit == '6':
                digit = '9'
            elif digit == '9':
                digit = '6'
            
            reversed_number += (int(digit)*10)**(length_n-1)
            length_n -= 1

        if reversed_number == n:
            return False
        return True
