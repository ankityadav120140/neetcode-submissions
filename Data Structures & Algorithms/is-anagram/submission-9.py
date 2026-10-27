class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dicS = {}
        dicT = {}

        for ch in s:
            if ch not in dicS:
                dicS[ch] = 1
            else:
                dicS[ch] += 1
        for ch in t:
            if ch not in dicT:
                dicT[ch] = 1
            else:
                dicT[ch] += 1
        
        return dicS == dicT