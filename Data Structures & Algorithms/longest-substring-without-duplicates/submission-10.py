class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        seen = {}

        for r in range(len(s)):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
                print(l)
            
            seen[s[r]] = r
            ans = max(ans, r - l + 1)

        return ans
            