class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for index,i in enumerate(nums):
            if i == target:
                return index
                break
            elif i > target:
                return index
                break
            elif index == len(nums)-1:
                return index+1