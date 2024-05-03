class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_s, cnt_t = {}, {}
        
        for each_s in s:
            cnt_s[each_s] = cnt_s.get(each_s, 0) + 1

        for each_t in t:
            cnt_t[each_t] = cnt_t.get(each_t, 0) + 1

        return cnt_s == cnt_t