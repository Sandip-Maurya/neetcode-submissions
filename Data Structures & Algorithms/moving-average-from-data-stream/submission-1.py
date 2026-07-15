class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.last_n = []

    def next(self, val: int) -> float:
        
        self.last_n.append(val)
        return sum(self.last_n[-self.size:])/min(self.size, len(self.last_n))
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
