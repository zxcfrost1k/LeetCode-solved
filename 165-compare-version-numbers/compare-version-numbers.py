class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        v1_sum = 0
        v2_sum = 0

        for n in range(max(len(v1), len(v2))):
            if len(v1) <= n:
                v1.append("0")
            if len(v2) <= n:
                v2.append("0")

            if int(v1[n]) > int(v2[n]):
                v1_sum += 1
                break
            if int(v1[n]) < int(v2[n]):
                v2_sum += 1
                break
            
        if v1_sum < v2_sum:
            return -1
        elif v1_sum > v2_sum:
            return 1
        else:
            return 0

        