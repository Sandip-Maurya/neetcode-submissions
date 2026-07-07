class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            second = target - num
            if second in seen:
                return [seen[second], i]

            seen[num] = i