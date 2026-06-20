class Solution:
    def longestPalindrome(self, s: str) -> str:
        long = len(s)
        maxi = 0
        res = ''
        if s[0] == s[-1] and long < 3:
            return s
        for x1 in range(0, long):
            for x2 in range(x1 + 1, long + 1):
                s0 = s[x1:x2]
                if s0 == s0[::-1]:
                    k = len(s0)
                    if k > maxi:
                        maxi = k
                        res = s0
        return res