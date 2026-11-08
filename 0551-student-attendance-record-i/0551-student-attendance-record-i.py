class Solution:
    def checkRecord(self, s: str) -> bool:
        count_A = 0
        count_L = 0

        for i in s:
            if i == 'A':
                count_A += 1
                count_L = 0
            elif i == 'L':
                count_L += 1
                if count_L >= 3:
                    break
            else:
                count_L = 0
        if count_A < 2 and count_L < 3:
            return True
        else:
            return False