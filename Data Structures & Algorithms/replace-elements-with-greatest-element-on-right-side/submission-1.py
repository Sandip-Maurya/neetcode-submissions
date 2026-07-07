class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        greatest = -1

        for i in range(n-1, -1, -1):
            temp = arr[i]
            arr[i] = greatest
            greatest = max(greatest, temp)

        return arr


        