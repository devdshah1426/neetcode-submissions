class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [ch.lower() for ch in s if ch.isalnum()]
        left = 0
        n = len(s_list)
        right = len(s_list) - 1
        same = True
        while left < n // 2:
            if s_list[left] == s_list[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
