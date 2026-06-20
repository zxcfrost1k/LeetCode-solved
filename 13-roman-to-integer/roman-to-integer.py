class Solution:
    def romanToInt(self, s: str) -> int:
        per = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,

            'q': 4,
            'w': 9,
            'e': 40,
            'r': 90,
            't': 400,
            'y': 900
        }
        
        s = s.replace('IV', 'q').replace('IX', 'w').replace('IX', 'w').replace('XL', 'e').replace('XC', 'r').replace('CD', 't').replace('CM', 'y')
        return sum([per[i] for i in s])