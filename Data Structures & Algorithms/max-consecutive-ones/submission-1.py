class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutiveOnes = [0]
        onesCounter = 0
        for num in nums:
            if num == 1: onesCounter += 1
            else:
                if onesCounter > 0: consecutiveOnes.append(onesCounter)
                onesCounter = 0
        if onesCounter > 0: consecutiveOnes.append(onesCounter)

        return max(consecutiveOnes)