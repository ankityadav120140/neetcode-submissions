class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = len(nums)
        res = []
        for i in range(s):
            l = i
            r = s - 1
            while l < r:
                sm = nums[l] + nums[r] + nums[i]
                if(sm > 0):
                    r -= 1
                elif sm < 0:
                    l += 1
                else:
                    finalList = [nums[i],nums[l],nums[r]]
                    if finalList not in res:
                        res.append(finalList)
                    l += 1
                    r -= 1
        return res
