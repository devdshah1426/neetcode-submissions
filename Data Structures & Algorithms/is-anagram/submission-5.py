class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = set(s)
        chars_t = set(t)
        if chars_s == chars_t:
            return True
        else:
            return False

        