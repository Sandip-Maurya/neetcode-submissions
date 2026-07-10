class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        total_time = 0
        position = 0
        for i, ch in enumerate(word):
            new_posotion = keyboard.index(ch)
            total_time += abs(position - new_posotion)
            position = new_posotion

        return total_time
