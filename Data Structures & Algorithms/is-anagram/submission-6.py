class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in t:
            if i in dic and dic[i] > 0:
                dic[i] -= 1
            else:
                return False
        return True