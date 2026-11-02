class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in nums2:
            nums1.insert(m,i)
            nums1.remove(0)
            m += 1
        return nums1.sort()