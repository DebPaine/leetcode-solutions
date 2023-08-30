class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Time: O(n)
        Space: O(1)
        """
        # Remove non alphabets from string and convert string to lowercase
        s = "".join(filter(str.isalnum, s)).lower()

        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
