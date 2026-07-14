class Logger:

    def __init__(self):
        self.track = {} # unique word and the timestamp tracking 

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.track: # unique message
            self.track[message] = timestamp
            return True
        else: # message seen recently
            if timestamp - self.track[message] >= 10:
                self.track[message] = timestamp
                return True
            else:
                return False

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
