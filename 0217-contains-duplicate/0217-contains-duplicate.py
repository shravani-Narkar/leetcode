class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashset = set()

        for i in nums:        # 1   2      3          1
            if i in hashset:  #()  (1)   (1,2)      (1,2,3)
                return True                          #True
            hashset.add(i)    #(1)  (1,2)  (1,2,3)
        return False