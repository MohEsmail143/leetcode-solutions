class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for num in list(num_set):
            if (num - 1) in num_set:
                continue
            else:
                length = 1
                while (num + length) in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest