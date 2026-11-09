class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count_jewels = 0

        for i in jewels:
            for j in stones:
                if i == j:
                    count_jewels += 1

        return count_jewels