class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        length_dict = defaultdict(int)
        max_length = 0

        for i in range(len(nums)):
            # First check if element already in dict - skip if yes
            curr_num = nums[i]
            if length_dict[curr_num] > 0:
                continue
            
            # Get current length by checking behind and ahead
            curr_length = length_dict[curr_num - 1] + 1 + length_dict[curr_num + 1]
            
            # Insert element in dict with new count
            length_dict[curr_num] = curr_length

            # Update lengths for front and end
            front = curr_num - length_dict[curr_num - 1]
            length_dict[front] = curr_length

            back = curr_num + length_dict[curr_num + 1]
            length_dict[back] = curr_length

            max_length = max(max_length, curr_length)

            #print(f"{curr_num} - {curr_length} - {front} - {back}")


        return max_length