class Solution:
    def reverse(self, x: int) -> int:
        return int(str(abs(x))[::-1]) if x > 0 and 2**31  > int(str(abs(x))[::-1]) else int('-' + str(abs(x))[::-1]) if 2**31  > int(str(abs(x))[::-1]) else 0
        