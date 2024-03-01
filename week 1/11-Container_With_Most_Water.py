class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_ptr = 0
        right_ptr = len(height)-1
        max_area = min(height[left_ptr],height[right_ptr])*(right_ptr - left_ptr)
        while left_ptr != right_ptr:
            if height[left_ptr] >= height[right_ptr]:
                right_ptr -= 1
                min_height = min((height[left_ptr],height[right_ptr]))
            elif height[left_ptr] < height[right_ptr]:
                left_ptr += 1
                min_height = min(height[left_ptr],height[right_ptr])
            if min_height*(right_ptr - left_ptr) > max_area:
                max_area = min_height*(right_ptr - left_ptr)
        return max_area