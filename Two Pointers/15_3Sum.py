class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n**2) + O(nlogn) ~= O(n**2), since we first sort nums and then use nested loops to iterate over it
        Space: O(n)
        """
        # Sort nums so that we can use two pointers algorithm
        nums.sort()
        output = []

        for i, num in enumerate(nums):
            # If the current num is the same as the previous num, then we would have the same set of triplet again. This is because we would have already gotten all the triplet for the same num, so no point in iterating using it as the first element again.
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
                    # We now check if within the inner loop, the previous left and left and previous right and right values are same or not. If they are same, then we move left +1 or/and right -1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return output
