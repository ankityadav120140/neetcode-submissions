class Solution:
    def checkPermutaion(self,s1: str, s2: str) -> bool:
        count = {}
        for ch in s1:
            count[ch] = count.get(ch,0) + 1
        for ch in s2:
            count[ch] = count.get(ch,0) - 1
            if(count[ch] == -1):
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        l = 0
        r = l1 - 1

        while r < l2:
            if self.checkPermutaion(s1, s2[l:r + 1]):
                return True
            r += 1
            l += 1
        return False