class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = 1

        while (numbers[first] + numbers[second] != target):
            if numbers[first] + numbers[second] > target or second + 1 == len(numbers):
                first += 1
                second = first + 1
            else:
                second += 1

        return [first+1, second+1]