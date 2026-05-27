class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
    
        for i, num in enumerate(nums):
            # Since nums is sorted, if index i corresponds to
            # positive number, there are no possible sums to 0
            if num > 0: 
                break

            # Avoid duplicates by making sure current nums[i]
            # does not equal nums[i-1]
            if i > 0 and num == nums[i-1]:
                continue

            # use j and k as pointers, starting outward-in
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = num + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    result.append([num, nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # again, shift j to avoid duplicates
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
            
        return result