class Solution:
    def isValid(self, s: str) -> bool:
        for _ in range(len(s) // 2):
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        if s == '':
            return True
        return False
