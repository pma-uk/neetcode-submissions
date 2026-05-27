class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Frequency arrays for 26 lowercase letters
        s1_count = [0] * 26
        window_count = [0] * 26

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        for i, c in enumerate(s2):
            window_count[ord(c) - ord('a')] += 1

            # Once the window is larger than s1, remove the leftmost char
            if i >= len(s1):
                left_char = s2[i - len(s1)]
                window_count[ord(left_char) - ord('a')] -= 1

            # Compare counts only when window size matches s1
            if window_count == s1_count:
                return True

        return False