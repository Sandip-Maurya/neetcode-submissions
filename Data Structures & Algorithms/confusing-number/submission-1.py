class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid_digits = {'2', '3', '4', '5', '7'}
        str_n = str(n)
        for invalid_digit in invalid_digits:
            if invalid_digit in str_n:
                return False

        str_n = str_n.replace('6', 'nine').replace('9', 'six')
        str_n = str_n.replace('nine', '9').replace('six', '6')
        if int(str_n[::-1]) == n:
            return False
        return True

