class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
       sorted_array = {}
       for id , val in nums1:
           sorted_array[id] = sorted_array.get(id,0) + val
       for id , val in nums2:
           sorted_array[id] = sorted_array.get(id,0) + val
       arr = []
       for key,values in sorted_array.items():
            arr.append([key,values])
       arr.sort()
       return arr