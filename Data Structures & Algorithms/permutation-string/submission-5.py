class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            ch1 = s1[i]
            index = ord(ch1) - ord('a')
            s1Count[index] += 1
            ch2 = s2[i]
            index = ord(ch2) - ord('a')
            s2Count[index] += 1
   
        if s1Count == s2Count:
            return True
            
        l = 0
        for r in range(len(s1), len(s2)):
            charL = s2[l]
            charR = s2[r]
            indexL = ord(charL) - ord('a')
            indexR = ord(charR) - ord('a')
            s2Count[indexL] -= 1
            s2Count[indexR] += 1
    
            if s2Count == s1Count:
                return True
            l += 1
        return False

