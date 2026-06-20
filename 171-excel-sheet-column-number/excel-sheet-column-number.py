class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letters = {chr(ord('A') + i): i + 1 for i in range(26)}

        n = 0
        for i in range(len(columnTitle)):
            n += letters[columnTitle[i]] * 26 ** (len(columnTitle) - i - 1)
        
        return n