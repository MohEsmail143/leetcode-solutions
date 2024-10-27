class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        vol = 0

        while l < r:
            if max_left <= max_right:
                l += 1
                max_left = max(max_left, height[l])
                vol += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                vol += max_right - height[r]

        return vol
