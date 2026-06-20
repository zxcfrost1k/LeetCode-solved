class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        numbers = {i: chr(ord('A') + i) for i in range(26)}

        s = ''
        while columnNumber > 0:
            columnNumber -= 1
            s = numbers[columnNumber % 26] + s
            columnNumber //= 26

        return s
