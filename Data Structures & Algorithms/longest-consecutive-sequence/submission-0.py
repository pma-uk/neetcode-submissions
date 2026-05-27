class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        length_dict = {}
        max_length = 1

        for i in range(len(nums)):
            # First check if element already in dict - skip if yes
            curr_num = nums[i]
            if curr_num in length_dict:
                continue
            
            # Get current length by checking behind and ahead
            curr_length = 1
            if (curr_num - 1) in length_dict:
                curr_length += length_dict[curr_num - 1]
            if (curr_num + 1) in length_dict:
                curr_length += length_dict[curr_num + 1]
            
            # Insert element in dict with new count
            length_dict[curr_num] = curr_length

            # Update lengths for front and end
            front = curr_num
            back = curr_num
            while (front - 1) in length_dict:
                front -= 1
            length_dict[front] = curr_length

            while (back + 1) in length_dict:
                back += 1
            length_dict[back] = curr_length

            max_length = max(max_length, curr_length)


        return max_length