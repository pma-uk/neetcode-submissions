class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            j = s.index('#', i)  # Find the delimiter for the length
            length = int(s[i:j])  # Extract the length
            i = j + 1 + length  # Move to the end of the current string
            result.append(s[j + 1:i])
        return result