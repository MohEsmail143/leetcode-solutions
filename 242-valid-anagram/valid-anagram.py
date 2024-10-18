from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = defaultdict(int)
        for c in s:
            s_dict[c] += 1
        for c in t:
            if c not in s_dict.keys():
                return False
            s_dict[c] -= 1
            if s_dict[c] < 0:
                return False
        return True