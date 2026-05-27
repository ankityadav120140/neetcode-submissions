class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        ignore = ['?',','," ",'\'','.',':']
        while l <= r:
            if(s[l] in ignore):
                l += 1
                continue

            if(s[r] in ignore):
                r -= 1
                continue
                
            if(s[l].lower() == s[r].lower()):
                l += 1
                r -= 1

            else:
                return False
        return True