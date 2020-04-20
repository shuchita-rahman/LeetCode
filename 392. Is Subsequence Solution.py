class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        flag = 0
        for i in s:
            for j in range(start, len(t)):
                if t[j] == i:
                    flag = flag +1
                    start = j +1
                    break
        if flag == len(s):
            return True
        return False
