class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for k in range(n):
            nums1[m + k] = nums2[k]
        nums1.sort()
        