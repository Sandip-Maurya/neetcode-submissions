class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        sub_strings = set()
        n = len(words)
        for i, outer_word in enumerate(words):
            for inner_word in words:
                if outer_word in inner_word and outer_word!=inner_word:
                    sub_strings.add(outer_word)
        return list(sub_strings)