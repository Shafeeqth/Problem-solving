class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        mid  = (len(nums3)) // 2
        return nums3[mid] if len(nums3) % 2 != 0 else (nums3[mid-1] + nums3[mid]) / 2
        