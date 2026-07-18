class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        r = k
        while r <= len(nums):
            ans.append(max(nums[r-k : r]))
            r += 1
        return ans
        