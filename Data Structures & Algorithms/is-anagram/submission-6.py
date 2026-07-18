class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        chars_s = set(s)
        chars_t = set(t)
        if chars_s == chars_t:
            return True
        else:
            return False

        