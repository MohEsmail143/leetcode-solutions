class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            if stack and h == stack[-1][1]:
                continue
            start_idx = i
            while stack and h < stack[-1][1]:
                start_idx = stack[-1][0]
                max_area = max((i - stack[-1][0]) * stack[-1][1], max_area)
                stack.pop()
            stack.append((start_idx, h))

        while stack:
            max_area = max((len(heights) - stack[-1][0]) * stack[-1][1], max_area)
            stack.pop()

        return max_area