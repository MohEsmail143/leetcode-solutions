class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master_list = []
        strs_dict_list = []

        for string in strs:
            string_dict = {}
            for c in string:
                string_dict[c] = string_dict.get(c, 0) + 1
            if string_dict in strs_dict_list:
                master_list[strs_dict_list.index(string_dict)].append(string)
            else:
                strs_dict_list.append(string_dict)
                master_list.append([string])

        return master_list