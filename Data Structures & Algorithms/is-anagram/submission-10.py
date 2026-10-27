class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = {}

        for ch in s:
            dic[ch] = dic.get(ch,0) + 1
        for ch in t:
            dic[ch] = dic.get(ch,0) -1
            if dic[ch] < 0:
                return False
        return True
