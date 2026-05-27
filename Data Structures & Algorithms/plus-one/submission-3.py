class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryOver = 1

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carryOver

            carryOver = digits[i] // 10
            digits[i] = digits[i] % 10

            if carryOver == 0:
                break
            elif i == 0:
                digits.insert(0, carryOver)

        return digits