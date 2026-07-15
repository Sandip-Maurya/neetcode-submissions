class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.last_n = []
        self.init_size = 0

    def next(self, val: int) -> float:
        
        self.last_n.append(val)
        if self.init_size < self.size:
            self.init_size += 1
            return sum(self.last_n[-self.size:])/self.init_size

        return sum(self.last_n[-self.size:])/self.size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
