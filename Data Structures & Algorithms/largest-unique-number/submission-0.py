class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums, reverse=True)

        nums_sorted_extended = [nums_sorted[0] + 1] + nums_sorted + [nums_sorted[-1]-1]
        for i, num in enumerate(nums_sorted, start=1):
            if nums_sorted_extended[i-1] > num > nums_sorted_extended [i+1]:
                return num  
        return -1