class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time: O(n), where n is the length of nums
        Space: O(1)
        """
        # answer[i] = prefix[i] * postfix[i]

        output = [1]
        temp_1 = temp_2 = 1

        for num in nums[: len(nums) - 1]:
            temp_1 *= num
            output.append(temp_1)

        for i in range(len(nums) - 1, 0, -1):
            temp_2 *= nums[i]
            output[i - 1] *= temp_2

        return output
