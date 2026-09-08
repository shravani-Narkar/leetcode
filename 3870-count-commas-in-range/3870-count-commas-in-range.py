class Solution:
    def countCommas(self, n: int) -> int:
        count = 0

        for i in range(1,n+1):
            if i >= 1000:
                count += 1
            #else:
            #    count == 0 
        return count               