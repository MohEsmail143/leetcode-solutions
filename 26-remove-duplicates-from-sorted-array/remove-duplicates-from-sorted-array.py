class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        to_delete = []
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while nums[i] == nums[j]:
                to_delete.append(j)
                j += 1
                if j >= len(nums):
                    break
            
            i = j

        for i in to_delete[::-1]:
            del nums[i]
            
        return len(nums)