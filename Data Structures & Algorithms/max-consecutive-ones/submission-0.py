class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_consecutive = 0
        current_consecutive = 0
        nums_extended = [0] + nums + [0]

        for i, num in enumerate(nums_extended):
            
            if num == 1:
                # consecutive 1's continue
                if nums_extended[i-1] == 1:
                    current_consecutive += 1
                # consecutive 1's break
                else:
                    current_consecutive = 1

            if current_consecutive > max_consecutive:
                max_consecutive = current_consecutive

            print(num, current_consecutive, max_consecutive)
            
        return max_consecutive
