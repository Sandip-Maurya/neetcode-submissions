class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            second = target - num
            if second in nums:
                j = nums.index(second)
                if i != j:
                    return sorted([i, j])
        