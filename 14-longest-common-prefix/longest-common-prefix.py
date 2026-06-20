class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_sort = sorted(strs, key=len)
        res = ''
        
        pre = []
        for i in range(0, len(strs_sort[-1])):
            pre.append(strs_sort[-1][:(i + 1)])
        
        for k in pre:
            if all(x.startswith(k) for x in strs):
                res = k
        
        return res