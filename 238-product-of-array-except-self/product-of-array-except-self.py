class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [nums[0]]
        right = [nums[-1]]
        rev_nums = nums[::-1]
        for i in range(1, len(nums)):
            left.append(nums[i] * left[i - 1])
            right.append(rev_nums[i] * right[i - 1])
        right = right[::-1]

        res = [right[1]]
        for i in range(1, len(nums) - 1):
            res.append(left[i-1] * right[i+1])
        res.append(left[-2])
        
        return res