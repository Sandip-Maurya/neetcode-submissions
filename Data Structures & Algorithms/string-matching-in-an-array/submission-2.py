class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        sub_strings = []
        n = len(words)
        for i, outer_word in enumerate(words):
            for j, inner_word in enumerate(words):
                if i==j or outer_word == inner_word or outer_word in sub_strings:
                    continue
                if outer_word in inner_word and outer_word!=inner_word:
                    sub_strings.append(outer_word)
        return sub_strings