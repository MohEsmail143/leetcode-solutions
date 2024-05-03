class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for x in nums:
            if x in num_dict.keys() and num_dict[x] == 1:
                return True
            num_dict[x] = 1
        return False