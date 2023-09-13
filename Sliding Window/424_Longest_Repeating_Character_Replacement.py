class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Time: O(n), where n is len(s)
        Space: O(26) ~= O(1)
        """
        l, r = 0, 0
        char_count = [0] * 26
        output = 0

        while l <= r < len(s):
            char_count[ord(s[r]) - ord('A')] += 1
            sw = r - l + 1

            # We need to find how many characters to replace in a given sliding window
            replacement = sw - max(char_count)

            if replacement > k:
                char_count[ord(s[l]) - ord('A')] -= 1
                l += 1
            else:
                output = max(output, sw)
            r += 1

        return output
