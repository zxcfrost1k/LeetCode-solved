class Solution:
    def reverseBits(self, n: int) -> int:
        n_b = f'{n:b}'

        if len(n_b) < 32:
            n_b = '0' * (32 - len(n_b)) + n_b

        n_b_reverse = n_b[::-1]

        return int(n_b_reverse, 2)