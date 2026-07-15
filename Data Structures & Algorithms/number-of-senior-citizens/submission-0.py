class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        senior_citizens = 0

        for passenger in details:
            age = int(passenger[-4:-2])
            if age > 60:
                senior_citizens += 1
        return senior_citizens
