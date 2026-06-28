class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        if numRows == 0:
            return res
        
        res.append([1])

        for i in range(1, numRows):
            cur_row = [1]
            pre_row = res[i - 1]

            for j in range(1, i):
                cur_row.append(pre_row[j - 1] + pre_row[j])
            
            cur_row.append(1)
            res.append(cur_row)
        
        return res

        
        
