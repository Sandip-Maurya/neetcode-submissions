class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        # rows = len(words)
        
        for row, word in enumerate(words):
            for column, ch in enumerate(word):
                try:
                    complementry_ch = words[column][row]
                    if not complementry_ch == ch:
                        return False
                except IndexError:
                    return False
        return True
                    

            