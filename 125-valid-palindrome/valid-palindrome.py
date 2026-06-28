class Solution:
    def isPalindrome(self, s: str) -> bool:
        return True if ''.join([char if char.isalnum() else '' for char in s]).lower() == ''.join([char if char.isalnum() else '' for char in s]).lower()[::-1] else False
