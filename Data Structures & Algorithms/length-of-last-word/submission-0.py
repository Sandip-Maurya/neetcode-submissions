class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_cleaned = s.strip()
        last_word = s_cleaned.split(" ")[-1]
        # print(last_word)
        return len(last_word.strip())