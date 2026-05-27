class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        seen_arr = []
        for key,v in seen.items():
            seen_arr.append(v)
        seen_arr.sort()
        seen_arr = seen_arr[-k:]

        ans = []
        for key,v in seen.items():
            if v in seen_arr:
                ans.append(key)
        return ans