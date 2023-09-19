class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time: O(m+n), where m is len(s1) and n is len(s2)
        Space: O(m+n)
        """
        c1, c2 = {}, {}
        sw = len(s1)

        for char in s1:
            c1[char] = 1 + c1.get(char, 0)

        for char in s2[:sw]:
            c2[char] = 1 + c2.get(char, 0)

        if c1 == c2:
            return True

        for i in range(len(s2) - sw):
            c2[s2[i]] -= 1
            # Delete the values which are 0
            if c2[s2[i]] == 0:
                del c2[s2[i]]
            c2[s2[i + sw]] = 1 + c2.get(s2[i + sw], 0)

            if c1 == c2:
                return True

        return False
