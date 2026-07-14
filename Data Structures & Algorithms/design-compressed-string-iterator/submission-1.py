class StringIterator:

    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        

    def next(self) -> str:
        import re
        pattern = r'([a-zA-Z])(\d+)([a-zA-Z]?)'
        match = re.match(pattern, self.compressedString)
        char, times_str, _ = match.groups()
        end = match.end()
        times = int(times_str)
        # print(char, times, end)
        # print(self.compressedString)
        if times == 1:
            self.compressedString = self.compressedString[2:]
        else:
            self.compressedString = f"{char}{times-1}{self.compressedString[end-1:]}"

        return char 
        

    def hasNext(self) -> bool:
        if self.compressedString:
            return True
        return False


# Your StringIterator object will be instantiated and called as such:
# compressedString = "N1e2t1C1o1d1e1f2"
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
