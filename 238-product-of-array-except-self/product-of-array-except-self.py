class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        n = len(nums)
        pre = 1
        for i in range(n - 1):
            pre *= nums[i]
            res.append(pre)
        
        post = 1
        for i in range(n - 1, 0, -1):
            post *= nums[i]
            res[i-1] *= post
        
        return res