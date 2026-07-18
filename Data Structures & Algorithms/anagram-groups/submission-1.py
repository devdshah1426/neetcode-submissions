class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_group = {}

        for word in strs:
            sorted_key = tuple(sorted(word))

            if sorted_key in anagrams_group:
                anagrams_group[sorted_key].append(word)
            else:
                anagrams_group[sorted_key] = [word]

        return list(anagrams_group.values())