class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [ch.lower() for ch in s if ch.isalnum()]

        left = 0
        right = len(s_list) - 1

        while left < right:
            if s_list[left] != s_list[right]:
                return False
            left += 1
            right -= 1

        return True
