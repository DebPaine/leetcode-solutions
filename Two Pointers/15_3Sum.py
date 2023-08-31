class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n**2) + O(nlogn) ~= O(n**2), since we first sort nums and then use nested loops to iterate over it
        Space: O(n)
        """
        output = []

        # Sort nums so that we can use two pointers algorithm
        nums.sort()

        for i, num in enumerate(nums):
            # We don't have to add the duplicate nums we find when i==0 since we can add the first set of nums if they add up to 0, for the next set we can skip it
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = num + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    output.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return output
