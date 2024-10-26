class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) < 3:
            return 0
        
        vol = 0

        m = 1
        max_left = height[0]
        max_right = max(height[2:])
        while m < len(height) - 1:
            vol += max(0, min(max_left, max_right) - height[m])
            max_left = max(max_left, height[m])
            max_right = max(height[m+1:])
            m += 1           

        return vol