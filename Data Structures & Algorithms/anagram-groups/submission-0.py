class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_table = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in anagram_table:
                anagram_table[sorted_str].append(str)
            else:
                 anagram_table[sorted_str] = [str]
        return list(anagram_table.values())
        