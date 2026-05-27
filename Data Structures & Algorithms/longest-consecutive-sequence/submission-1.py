class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        nums.sort()
        ans = 1
        tempRange = 1
        lastVisit = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] - lastVisit == 1:
                tempRange += 1
                lastVisit = nums[i]
            else:
                ans = max(ans, tempRange)
                tempRange = 1
                lastVisit = nums[i]

        return max(ans,tempRange)
