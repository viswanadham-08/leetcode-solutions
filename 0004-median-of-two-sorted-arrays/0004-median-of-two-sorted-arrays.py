class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       m = len(nums1)+len(nums2)
       merged_array = nums1 + nums2
       merged_array.sort()
       if m % 2 ==0 :
          median = (merged_array[m//2] + merged_array[(m//2-1)])/2
       else :
          median = merged_array[m//2]
       return median 