class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        char_freq = {}

        for char in s:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1 
        
        odd_count = 0
        for char, freq in char_freq.items():
            if freq % 2 != 0: # odd
                if odd_count > 0:
                    return False
                odd_count += 1
        return True
            



        