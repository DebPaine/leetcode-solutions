class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(n), where n is the length of nums
        Space: O(n)
        """
        count = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        output = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, count in count.items():
            bucket[count].append(num)

        for sublist in bucket[::-1]:
            if sublist:
                output += sublist

        return output[:k]
