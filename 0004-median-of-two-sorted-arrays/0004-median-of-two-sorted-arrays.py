class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0 and len(nums2) == 0:
            return 0.0
        if len(nums1) == 1 and len(nums2) == 0:
            return nums1[0]
        if len(nums1) == 0 and len(nums2) == 1:
            return nums2[0]

        integrated = sorted(list(nums1 + nums2))

        if len(integrated) % 2 == 0:
            right_idx = len(integrated) // 2
            left_idx = right_idx - 1
            return (integrated[left_idx] + integrated[right_idx]) / 2
        else:
            mid_idx = len(integrated) // 2
            return integrated[mid_idx]
            # 1, 2, 3, 4, 5 5 / 2
            # -1 0 1 2 / 2
            # 0, 1, 4, 5, 10, 11, 20 7 / 2 = 3


        