from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        res = []
        for _ in range(k):
            max_v = 0
            max_k = 0
            for k, v in nums_count.items():
                if max_v < v:
                    max_v = v
                    max_k = k
            res.append(max_k)
            nums_count.pop(max_k)
        return res
