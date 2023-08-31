class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Time: O(n), where n is the no. of heights or length of heights list
        Space: O(1)
        """
        area = 0

        left, right = 0, len(height) - 1
        while left < right:
            # The min height of left and right decides the height of the container
            min_height = min(height[left], height[right])
            area = max(area, (right - left) * min_height)

            # We move left +1 since the min height between left and right determines the height of the container and so, we move left since that there is a possibility of finding an higher height which can potentially increase the container area
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1

        return area
