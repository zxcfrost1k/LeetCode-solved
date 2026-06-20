class Solution:
    def myAtoi(self, s: str) -> int:
        nums = '1234567890'
        flag = True
        x0 = s.strip()
        if len(x0) == 0:
            return 0
        x00 = ''
        if x0[0] == '-':
            flag = False
            x0 = x0[1:]
        elif x0[0] == '+':
            x0 = x0[1:]
        for k in x0:
            if k in nums:
                x00 += k
            else:
                break
        if len(x00) == 0:
            return 0
        if flag:
            f = int(x00)
        else:
            f = -int(x00)
        g = 2 ** 31
        if -g <= f <= g - 1:
            return f
        if  f < -g:
            return -g
        if f > g - 1:
            return g - 1