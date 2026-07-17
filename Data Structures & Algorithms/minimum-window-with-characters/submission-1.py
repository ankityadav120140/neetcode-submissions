class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        
        for ch in t:
            tMap[ch] = tMap.get(ch,0) + 1
        
        need = len(tMap)
        have = 0

        window = {}

        res = ""

        l = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch,0) + 1
            if ch in tMap and window[ch] == tMap[ch]:
                have += 1
            while have == need:
                if res == "" or len(s[l:r + 1]) < len(res):
                        res = s[l:r+1]
                window[s[l]] -= 1
                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    have -= 1     
                l += 1
        return res
