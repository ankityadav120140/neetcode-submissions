class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        r = 1

        while l < len(s) and r < len(s):
            print(s[l:r])
            if s[r] in s[l:r]:
                ans = max(ans, r - l)
                l = r
                r += 1
            else:
                r += 1
        
        return ans