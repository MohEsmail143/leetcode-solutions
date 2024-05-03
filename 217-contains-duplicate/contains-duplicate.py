class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for x in nums:
            if x in num_set:
                return True
            else:
                num_set.add(x)
        return False