class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l = len(heights)
        for i in range(l):
            for j in range(i+1,l):
                ar = min(heights[i],heights[j]) * (j - i)
                ans = max(ar,ans)
        return ans