class Solution:
    def isPalindrome(self, s: str) -> bool:
        singleString = [char.lower() for char in s if char.isalnum()]

        leftPointer = 0
        rightPointer = len(singleString) - 1

        while leftPointer <= rightPointer:
            if singleString[leftPointer] != singleString[rightPointer]:
                return False

            leftPointer += 1
            rightPointer -= 1

        return True