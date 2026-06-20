class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        
        s = "".join(sorted(s1))

        l = 0
        r = l1 - 1

        while r < l2:
            if "".join(sorted(s2[l:r + 1])) == s:
                return True
            r += 1
            l += 1
        return False