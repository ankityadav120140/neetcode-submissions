class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        buckets = [[] for _ in range(len(nums) + 1)]

        for key,value in seen.items():
            buckets[value].append(key)
            
        ans = []
        for i in range(len(buckets)-1, 0, -1):
            for j in buckets[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans
        return ans
        