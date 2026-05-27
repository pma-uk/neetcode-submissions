class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        orphanStack = [] # Holds indexes of temps that haven't yet been matched with warmer temp

        for i in range(len(temperatures)):
            # If orphan temps exist AND they are colder than current, update results
            while orphanStack and temperatures[i] > temperatures[orphanStack[-1]]:
                orphanIndex = orphanStack.pop()
                result[orphanIndex] = i - orphanIndex
            
            orphanStack.append(i)

        return result