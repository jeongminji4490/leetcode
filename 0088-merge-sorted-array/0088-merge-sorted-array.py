class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        sorted_arr = []
        n1 = n2 = 0
        while n1 < m and n2 < n:
            if nums1[n1] < nums2[n2]:
                sorted_arr.append(nums1[n1])
                n1 += 1
            else:
                sorted_arr.append(nums2[n2])
                n2 += 1
        while n1 < m:
            sorted_arr.append(nums1[n1])
            n1 += 1
        while n2 < n:
            sorted_arr.append(nums2[n2])
            n2 += 1

        for i in range(n + m):
            nums1[i] = sorted_arr[i]

        