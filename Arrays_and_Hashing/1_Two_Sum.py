class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """

        complement = {}

        for i, num in enumerate(nums):
            if target - num in complement:
                return [i, complement[target - num]]
            else:
                complement[num] = i

        return []
