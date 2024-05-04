class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_set_list = list(set(nums))
        num_dict = {}
        for x in num_set_list:
            num_dict[x] = nums.count(x)
        return list({x: y for x, y in sorted(num_dict.items(), key=lambda item: item[1], reverse=True)})[:k]