class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_consecutive = 0
        current_consecutive = 0

        for i, num in enumerate(nums):
            
            if num == 1:
                current_consecutive += 1
                max_consecutive = max(max_consecutive, current_consecutive)
            else:
                current_consecutive = 0


        return max_consecutive
