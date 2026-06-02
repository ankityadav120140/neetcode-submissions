class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        ans = 0
        while r < len(s):
            if s[r] in s[l : r]:
                l += 1
            else:
                r += 1
            ans = max(ans,r - l)
        
        return ans
            