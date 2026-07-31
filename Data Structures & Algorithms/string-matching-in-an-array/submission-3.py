class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        sub_strings = []
        n = len(words)
        for i, outer_word in enumerate(words):
            for j, inner_word in enumerate(words):
                if outer_word in inner_word and i!=j:
                    sub_strings.append(outer_word)
                    break 
        return sub_strings