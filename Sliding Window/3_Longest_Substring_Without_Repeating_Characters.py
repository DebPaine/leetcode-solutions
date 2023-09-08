class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time: O(n), where n is the length of s
        Space: O(26) ~= O(1), since the english alphabet has 26 letters and set will have unique characters only
        """
        left, right, max_length = 0, 0, 0
        unique = set()

        while left <= right and right < len(s):
            if s[right] not in unique:
                unique.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                while s[right] in unique:
                    unique.remove(s[left])
                    left += 1

        return max_length
