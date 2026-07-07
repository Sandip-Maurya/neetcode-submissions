class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr = []
        arr_len = len(arr)
        for i, elem in enumerate(arr):
            if i == arr_len-1:
                new_arr.append(-1)
                return new_arr
            max_elem = max(arr[i+1:])
            new_arr.append(max_elem)
        return new_arr


        