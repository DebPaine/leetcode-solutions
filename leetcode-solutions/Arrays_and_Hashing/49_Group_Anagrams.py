class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time: O(m*n*26) ~= O(m*n), where m is the length of strs, n is the length of each string, and we are converting chars list to tuple of length 26
        Space: O(m*26) ~= O(m), where we are creating new chars list for every word in strs
        """

        char_count = {}  # Can use defaultdict(list) too

        for word in strs:
            chars = [0] * 26
            for char in word:
                # Lowercase alphabets ASCII value starts with 97, or ord('a')
                chars[ord(char) - ord("a")] += 1

            # list can't be used as a key in dict, and converting list to tuple is O(n) operation
            chars = tuple(chars)
            if chars in char_count:
                char_count[chars].append(word)
            else:
                char_count[chars] = [word]

        return char_count.values()
