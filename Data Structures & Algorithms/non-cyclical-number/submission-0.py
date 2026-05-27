class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquaredDigits(num: int) -> int:
            divisor = 1000
            squaredSum = 0

            while divisor >= 1:
                digit = num // divisor
                num = num % divisor

                squaredSum += digit**2

                divisor /= 10

            return int(squaredSum)

        seenNumsSet = set()
        seenNumsSet.add(n)
        
        while n > 1:
            n = sumSquaredDigits(n)
            if n in seenNumsSet:
                return False
            seenNumsSet.add(n)
        
        return True