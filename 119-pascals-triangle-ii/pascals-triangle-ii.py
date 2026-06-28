class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        res.append([1])

        if rowIndex == 0:
            return res[-1]

        for i in range(1, rowIndex + 1):
            pre_row = res[i - 1]
            cur_row = [1]

            for j in range(1, i):
                cur_row.append(pre_row[j - 1] + pre_row[j])

            cur_row.append(1)
            res.append(cur_row)

        return res[-1]