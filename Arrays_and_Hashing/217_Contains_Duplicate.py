class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """

        unique = set()

        for num in nums:
            if num in unique:
                return True
            else:
                unique.add(num)

        return False
