class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for num in nums1:
            output.append(nums2.index(num))
        return output
