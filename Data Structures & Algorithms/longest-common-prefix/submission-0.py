class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest_common_prefix = ""
        sorted_strs = sorted(strs)
        for first_word_char, last_word_char in zip(sorted_strs[0], sorted_strs[-1]):
            if first_word_char != last_word_char:
                return longest_common_prefix
            longest_common_prefix += first_word_char
        return longest_common_prefix


