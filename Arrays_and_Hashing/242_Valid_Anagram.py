class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(m+n), where m is the length of s and n is the length of t
        Space: O(m), since we are only storing the char count of s
        """

        # Convert all unicode characters (if any) to string
        s = "".join([str(char) for char in s])
        t = "".join([str(char) for char in t])

        if len(s) != len(t):
            return False

        s_count = {}

        for char in s:
            s_count[char] = 1 + s_count.get(char, 0)

        # Instead of storing t_count in another dict, we will use the same above dict and decrease char count by 1
        for char in t:
            s_count[char] = s_count.get(char, 0) - 1

        for k, v in s_count.items():
            if v != 0:
                return False

        return True
