class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in idx_dict.keys():
                return i, idx_dict[diff]
            idx_dict[nums[i]] = i
        return