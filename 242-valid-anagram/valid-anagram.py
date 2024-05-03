class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for l in list(set(t)):
            if s.count(l) != t.count(l):
                return False
        return True