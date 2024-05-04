class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        acc_l = 1
        acc_r = 1
        product_l = []
        product_r = []

        for i in range(len(nums)):
            acc_l *= nums[i]
            product_l.append(acc_l)

            acc_r *= nums[len(nums) - i - 1]
            product_r.insert(0, acc_r)

        answer = [product_r[1], product_l[-2]]
    
        for i in range(1, len(nums)-1):
            answer.insert(i, product_l[i-1] * product_r[i+1])
    
        return answer