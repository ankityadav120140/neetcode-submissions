class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        ans = 0
        for i in range(len(nums)):
            if(nums[i]-1 not in st):
                l = 1
                while nums[i] + l in st:
                    l += 1
                ans = max(ans, l)
        return ans