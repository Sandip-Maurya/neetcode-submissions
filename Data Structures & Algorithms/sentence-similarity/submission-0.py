class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        n1 = len(sentence1)
        n2 = len(sentence2)
        

        if n1 != n2 :
            return False

        for i in range(n1):
            word1 = sentence1[i]
            word2 = sentence2[i]
            if word1 == word2:
                continue
            if not ([word1, word2] in similarPairs or [word2, word1] in similarPairs):
                return False
        return True
            